"""Account Takeover (ATO) risk scorer."""

from decimal import Decimal
from typing import Any

from sentinel.feature_store import PayerFeatures
from sentinel.schemas import EvaluateRequest, SignalItem


def score_ato(request: EvaluateRequest, features: PayerFeatures) -> tuple[float, list[SignalItem]]:
    """Evaluate whether the proposed transaction reflects an unauthorized account takeover."""
    signals: list[SignalItem] = []
    total_points = 0
    max_possible_points = 12

    # 1. New device detection
    if request.session.is_new_device:
        points = 4
        total_points += points
        signals.append(
            SignalItem(
                key="new_device_access",
                signal_group="ato",
                points=points,
                observed=f"Dispositivo no reconocido: {request.session.device_id}",
                baseline=f"{len(features.known_devices)} dispositivos habituales registrados",
                explanation="El inicio de sesión proviene de un dispositivo nunca antes utilizado por el titular.",
            )
        )

    # 2. IP / Geo anomalous risk
    ip_risk = request.session.ip_risk
    geo_risk = request.session.geo_risk
    if ip_risk == "high" or geo_risk == "high":
        points = 3
        total_points += points
        signals.append(
            SignalItem(
                key="high_risk_network_or_geo",
                signal_group="ato",
                points=points,
                observed=f"IP risk: {ip_risk}, Geo risk: {geo_risk}",
                baseline="Conexiones habituales de bajo riesgo",
                explanation="La conexión se originó desde una red o ubicación geográfica catalogada como de alto riesgo.",
            )
        )
    elif ip_risk == "medium" or geo_risk == "medium":
        points = 1
        total_points += points
        signals.append(
            SignalItem(
                key="moderate_risk_network",
                signal_group="ato",
                points=points,
                observed=f"IP risk: {ip_risk}, Geo risk: {geo_risk}",
                baseline="Conexiones habituales",
                explanation="La red o ubicación presenta variaciones moderadas respecto al patrón normal.",
            )
        )

    # 3. Recent credential change
    if features.credential_changed_hours_ago is not None and features.credential_changed_hours_ago <= 24.0:
        points = 3
        total_points += points
        signals.append(
            SignalItem(
                key="recent_credential_modification",
                signal_group="ato",
                points=points,
                observed=f"Credenciales modificadas hace {features.credential_changed_hours_ago:.1f} horas",
                baseline="Sin cambios de seguridad en los últimos 30 días",
                explanation="Se modificó la contraseña o token de seguridad poco antes de solicitar la transferencia.",
            )
        )

    # 4. Unusual hour of transfer
    prop_hour = request.proposed_at.hour
    if features.usual_hours and prop_hour not in features.usual_hours and (prop_hour < 6 or prop_hour >= 23):
        points = 2
        total_points += points
        signals.append(
            SignalItem(
                key="atypical_nocturnal_hour",
                signal_group="ato",
                points=points,
                observed=f"Hora de operación: {prop_hour:02d}:00 hrs",
                baseline=f"Horario usual: {sorted(features.usual_hours)} hrs",
                explanation="La operación se intenta en un horario nocturno ajeno a la actividad histórica de la cuenta.",
            )
        )

    normalized_score = min(1.0, total_points / max_possible_points)
    return round(normalized_score, 4), signals
