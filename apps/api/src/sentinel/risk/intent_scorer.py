"""Payer Intent and Social Engineering Coercion risk scorer."""

from decimal import Decimal
from sentinel.feature_store import PayerFeatures
from sentinel.schemas import EvaluateRequest, SignalItem


def score_intent(request: EvaluateRequest, features: PayerFeatures) -> tuple[float, list[SignalItem]]:
    """Evaluate whether the genuine payer is behaving under psychological manipulation, urgency, or coaching."""
    signals: list[SignalItem] = []
    total_points = 0
    max_possible_points = 20

    amt = request.amount

    # 1. Amount substantially exceeding 90-day historical maximum
    if features.transfer_count_90d > 0 and features.max_amount_90d > Decimal("0.00"):
        if amt >= features.max_amount_90d * Decimal("2.0"):
            points = 4
            total_points += points
            signals.append(
                SignalItem(
                    key="amount_drastically_exceeds_baseline",
                    signal_group="intent",
                    points=points,
                    observed=f"${amt:,.2f} MXN solicitados",
                    baseline=f"Máximo histórico en 90 días: ${features.max_amount_90d:,.2f} MXN",
                    explanation="El monto solicitado supera drásticamente cualquier transferencia previa realizada por el cliente.",
                )
            )
        elif amt >= features.max_amount_90d * Decimal("1.3"):
            points = 2
            total_points += points
            signals.append(
                SignalItem(
                    key="amount_above_typical_baseline",
                    signal_group="intent",
                    points=points,
                    observed=f"${amt:,.2f} MXN solicitados",
                    baseline=f"Promedio habitual: ${features.avg_amount_90d:,.2f} MXN",
                    explanation="El monto es notablemente más alto que el comportamiento típico reciente.",
                )
            )

    # 2. Balance exhaustion ratio (draining the account)
    if features.last_known_balance > Decimal("0.00"):
        drain_ratio = float(amt / features.last_known_balance)
        if drain_ratio >= 0.80:
            points = 4
            total_points += points
            signals.append(
                SignalItem(
                    key="severe_balance_drain",
                    signal_group="intent",
                    points=points,
                    observed=f"Drenando el {drain_ratio * 100:.1f}% del saldo estimado",
                    baseline="Retención de liquidez habitual",
                    explanation="La operación dejaría la cuenta prácticamente en ceros, patrón característico de fraude por coerción.",
                )
            )
        elif drain_ratio >= 0.50:
            points = 2
            total_points += points
            signals.append(
                SignalItem(
                    key="moderate_balance_drain",
                    signal_group="intent",
                    points=points,
                    observed=f"Comprometiendo el {drain_ratio * 100:.1f}% del saldo",
                    baseline="Saldos residuales seguros",
                    explanation="La operación consume una proporción inusualmente alta de los fondos disponibles.",
                )
            )

    # 3. Beneficiary registration freshness
    if features.beneficiary_created_minutes_ago is not None:
        mins = features.beneficiary_created_minutes_ago
        if mins <= 15.0:
            points = 4
            total_points += points
            signals.append(
                SignalItem(
                    key="beneficiary_registered_moments_ago",
                    signal_group="intent",
                    points=points,
                    observed=f"Beneficiario dado de alta hace {mins:.1f} minutos",
                    baseline="Transferencias habituales a contactos consolidados",
                    explanation="La cuenta destino fue registrada hace escasos minutos, típico de estafadores guiando el alta en vivo.",
                )
            )
        elif mins <= 60.0:
            points = 2
            total_points += points
            signals.append(
                SignalItem(
                    key="beneficiary_registered_recently",
                    signal_group="intent",
                    points=points,
                    observed=f"Beneficiario registrado hace {mins:.1f} minutos",
                    baseline="Contactos frecuentes",
                    explanation="El destinatario fue registrado en la última hora.",
                )
            )

    # 4. Burst velocity in the last hour
    if features.velocity_1h_count >= 2:
        points = 4
        total_points += points
        signals.append(
            SignalItem(
                key="unusual_hourly_velocity_burst",
                signal_group="intent",
                points=points,
                observed=f"{features.velocity_1h_count} transferencias previas en los últimos 60 min (${features.velocity_1h_amount:,.2f} MXN)",
                baseline="Frecuencia habitual: 0 a 1 transferencia diaria",
                explanation="Ráfaga anormal de pagos concentrados en un lapso breve de tiempo.",
            )
        )

    # 5. Regulatory MTU cap structuring (staying just below the 1,500 UDIs limit ~ $12,800 MXN)
    if Decimal("9500.00") <= amt <= Decimal("12800.00"):
        if not features.is_destination_clabe_known or features.velocity_1h_count >= 1:
            points = 4
            total_points += points
            signals.append(
                SignalItem(
                    key="mtu_regulatory_cap_structuring",
                    signal_group="intent",
                    points=points,
                    observed=f"${amt:,.2f} MXN (muy cerca del tope MTU de 1,500 UDIs ≈ $12,800 MXN)",
                    baseline="Montos variados según necesidad",
                    explanation="Monto diseñado para evitar los filtros automáticos regulatorios del tope MTU.",
                )
            )

    # 6. Limit raised and immediately utilized
    if features.limit_changed_minutes_ago is not None and features.limit_changed_minutes_ago <= 60.0:
        points = 4
        total_points += points
        ratio_str = f" ({features.limit_change_ratio:.1f}x incremento)" if features.limit_change_ratio else ""
        signals.append(
            SignalItem(
                key="limit_increased_immediately_prior",
                signal_group="intent",
                points=points,
                observed=f"Límite aumentado hace {features.limit_changed_minutes_ago:.1f} minutos{ratio_str}",
                baseline="Límites estables en el tiempo",
                explanation="El usuario incrementó su límite de transferencia pocos minutos antes de ejecutar el pago, común al ser coaccionado por teléfono.",
            )
        )

    # 7. Active telephone call telemetry
    if request.context.active_call:
        points = 4
        total_points += points
        signals.append(
            SignalItem(
                key="concurrent_active_voice_call",
                signal_group="intent",
                points=points,
                observed="Llamada telefónica activa en simultáneo con la banca móvil",
                baseline="Operaciones bancarias habituales sin llamada concurrente",
                explanation="El usuario está en una llamada de voz mientras opera su banca, fuerte indicio de estafa por ingeniería social (falso ejecutivo/secuestro virtual).",
            )
        )

    # 8. Remote screen share or remote desktop control
    if request.context.screen_share or request.context.remote_access:
        points = 5
        total_points += points
        observed_tool = "Compartición de pantalla" if request.context.screen_share else "Acceso remoto activo"
        signals.append(
            SignalItem(
                key="remote_screen_share_detected",
                signal_group="intent",
                points=points,
                observed=observed_tool,
                baseline="Sin software de acceso remoto en el dispositivo",
                explanation="Se detectó software de visualización o control remoto activo durante la transacción.",
            )
        )

    normalized_score = min(1.0, total_points / max_possible_points)
    return round(normalized_score, 4), signals
