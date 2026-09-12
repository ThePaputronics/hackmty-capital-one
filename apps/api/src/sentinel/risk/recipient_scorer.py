"""Recipient Network and Destination CLABE risk scorer."""

from datetime import timedelta
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from sentinel.feature_store import PayerFeatures
from sentinel.models import Event
from sentinel.schemas import EvaluateRequest, SignalItem


def score_recipient(
    request: EvaluateRequest,
    features: PayerFeatures,
    db: Session | None = None,
) -> tuple[float, list[SignalItem]]:
    """Evaluate destination CLABE and counterparty institution risks."""
    signals: list[SignalItem] = []
    total_points = 0
    max_possible_points = 10

    # 1. Payer has never transferred to this CLABE
    if not features.is_destination_clabe_known:
        points = 3
        total_points += points
        signals.append(
            SignalItem(
                key="first_time_destination_clabe",
                signal_group="recipient",
                points=points,
                observed=f"CLABE {request.destination_clabe[:6]}...{request.destination_clabe[-4:]} nunca antes vista",
                baseline=f"{len(features.known_beneficiary_clabes)} cuentas destino registradas en el historial",
                explanation="Es la primera vez que este pagador envía dinero a esta CLABE interbancaria.",
            )
        )

    # 2. Payer has never transferred to this banking institution
    if not features.is_destination_institution_known:
        points = 2
        total_points += points
        signals.append(
            SignalItem(
                key="unseen_destination_institution",
                signal_group="recipient",
                points=points,
                observed=f"Institución {request.destination_institution_code} sin antecedentes en esta cuenta",
                baseline=f"Bancos habituales: {', '.join(sorted(features.known_institutions)) or 'Ninguno'}",
                explanation="El usuario nunca ha operado hacia esta entidad bancaria o fintech receptora.",
            )
        )

    # 3. Destination registered moments prior to transfer
    if features.beneficiary_created_minutes_ago is not None and features.beneficiary_created_minutes_ago <= 60.0:
        points = 2
        total_points += points
        signals.append(
            SignalItem(
                key="newly_registered_recipient",
                signal_group="recipient",
                points=points,
                observed=f"Destinatario registrado hace {features.beneficiary_created_minutes_ago:.1f} minutos",
                baseline="Destinatarios con antigüedad en la agenda",
                explanation="El beneficiario fue dado de alta escasos momentos antes de la transferencia.",
            )
        )

    # 3. Cross-payer rapid fan-in (Rail anomaly signature: multiple distinct payers funding the same CLABE in 24h)
    if db is not None:
        window_24h = request.proposed_at - timedelta(hours=24)
        stmt = (
            select(func.count(func.distinct(Event.payer_id)))
            .where(
                Event.type == "transfer_settled",
                Event.occurred_at >= window_24h,
                Event.occurred_at <= request.proposed_at,
                func.json_extract(Event.payload, "$.destination_clabe") == request.destination_clabe,
            )
        )
        try:
            distinct_payers = db.execute(stmt).scalar() or 0
            if distinct_payers >= 3:
                points = 4
                total_points += points
                signals.append(
                    SignalItem(
                        key="rapid_fan_in_destination_cluster",
                        signal_group="recipient",
                        points=points,
                        observed=f"{distinct_payers} ordenantes distintos enviaron fondos a esta CLABE en las últimas 24h",
                        baseline="Recepción habitual entre particulares",
                        explanation="La cuenta receptora presenta un volumen anómalo de ingresos simultáneos de múltiples personas (patrón mulero de captación).",
                    )
                )
        except Exception:
            # Fallback if json_extract differs across engines or dialect
            pass

    normalized_score = min(1.0, total_points / max_possible_points)
    return round(normalized_score, 4), signals
