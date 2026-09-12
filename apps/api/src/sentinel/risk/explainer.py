"""Customer explanation templates and reason code generation in Spanish."""

from typing import Protocol
from sentinel.schemas import SignalItem


class Explainer(Protocol):
    """Protocol for generating customer-facing warnings in Spanish."""

    def explain(
        self,
        decision: str,
        reason_codes: list[str],
        signals: list[SignalItem],
        payer_first_name: str | None = None,
    ) -> str:
        """Generate compassionate, actionable Spanish guidance."""
        ...


class TemplateExplainer:
    """Deterministic, auditable Spanish template explainer."""

    TEMPLATES = {
        "allow": (
            "Transferencia validada de manera habitual. No se detectaron anomalías en tu operación."
        ),
        "challenge_call_and_destination": (
            "⚠️ Detectamos que estás en una llamada telefónica mientras registras un destinatario nuevo. "
            "Si alguien te dijo por teléfono que es tu banco, soporte técnico o un familiar en problemas: "
            "LOS BANCOS NUNCA SOLICITAN TRANSFERIR DINERO PARA 'PROTEGERLO' NI PARA 'CANCELAR UN CARGO'. "
            "Por favor confirma con calma si realmente conoces a esta persona."
        ),
        "challenge_high_amount_new_dest": (
            "⚠️ Esta transferencia es considerablemente más alta que tus movimientos habituales y se dirige a una cuenta nueva. "
            "Por tu seguridad, solicitamos confirmar tu identidad con un paso de autenticación adicional antes de enviar los fondos."
        ),
        "challenge_generic": (
            "⚠️ Detectamos condiciones poco usuales en esta operación (destinatario no registrado y comportamiento atípico). "
            "Te pedimos verificar los datos antes de proceder."
        ),
        "pause_coercion_critical": (
            "Pausamos esta transferencia por señales de riesgo durante una llamada o acceso remoto. "
            "Cuelga y llama a tu banco usando su número oficial."
        ),
        "pause_ato_critical": (
            "Pausamos esta transferencia por actividad inusual en tu cuenta. "
            "Revisa tus movimientos y contacta a tu banco por un canal oficial."
        ),
        "pause_generic": (
            "Pausamos esta transferencia por varias señales de riesgo. "
            "Verifica los datos y contacta a tu banco por un canal oficial."
        ),
    }

    def explain(
        self,
        decision: str,
        reason_codes: list[str],
        signals: list[SignalItem],
        payer_first_name: str | None = None,
    ) -> str:
        """Produce the appropriate explanation based on corroborated reason codes."""
        if decision == "allow":
            return self.TEMPLATES["allow"]

        # If pausing due to coercion indicators
        if decision == "pause":
            if any(
                code in reason_codes
                for code in (
                    "ACTIVE_CALL_MANIPULATION",
                    "REMOTE_ACCESS_DETECTED",
                    "RAPID_COERCION_PLAYBOOK",
                )
            ):
                return self.TEMPLATES["pause_coercion_critical"]
            if any(code in reason_codes for code in ("NEW_DEVICE_ATO", "CREDENTIAL_HIJACK")):
                return self.TEMPLATES["pause_ato_critical"]
            return self.TEMPLATES["pause_generic"]

        # If challenging
        if "ACTIVE_CALL_MANIPULATION" in reason_codes or "NEW_DESTINATION_RISK" in reason_codes:
            return self.TEMPLATES["challenge_call_and_destination"]
        if "HIGH_AMOUNT_ANOMALY" in reason_codes:
            return self.TEMPLATES["challenge_high_amount_new_dest"]

        return self.TEMPLATES["challenge_generic"]


default_explainer = TemplateExplainer()
