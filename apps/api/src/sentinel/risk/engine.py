"""Risk decision engine enforcing multi-factor corroboration."""

import time
from decimal import Decimal
from typing import Any
from sqlalchemy.orm import Session

from sentinel.config import get_settings
from sentinel.feature_store import PayerFeatures
from sentinel.risk.ato_scorer import score_ato
from sentinel.risk.explainer import default_explainer
from sentinel.risk.intent_scorer import score_intent
from sentinel.risk.recipient_scorer import score_recipient
from sentinel.schemas import EvaluateRequest, EvaluateResponse, ScoresBreakdown, SignalItem


class RiskEngine:
    """Evaluates transfer requests and corroborates multi-dimensional evidence."""

    HIGH_THRESHOLD = 0.40  # A dimension is elevated when its normalized score >= 0.40

    @classmethod
    def evaluate(
        cls,
        request: EvaluateRequest,
        features: PayerFeatures,
        db: Session | None = None,
    ) -> tuple[str, ScoresBreakdown, list[SignalItem], list[str], str]:
        """Corroborate ATO, Intent, and Recipient signals to form a decision.

        Returns: (decision, scores, signals, reason_codes, payer_message_es)
        """
        # 1. Run individual dimension scorers
        ato_score, ato_signals = score_ato(request, features)
        intent_score, intent_signals = score_intent(request, features)
        recipient_score, recipient_signals = score_recipient(request, features, db=db)

        all_signals = ato_signals + intent_signals + recipient_signals

        # 2. Count elevated dimensions
        elevated_ato = ato_score >= cls.HIGH_THRESHOLD
        elevated_intent = intent_score >= cls.HIGH_THRESHOLD
        elevated_recipient = recipient_score >= cls.HIGH_THRESHOLD

        elevated_count = sum([elevated_ato, elevated_intent, elevated_recipient])

        # 3. Derive reason codes from detected signals
        reason_codes: list[str] = []
        signal_keys = {s.key for s in all_signals}

        if "new_device_access" in signal_keys:
            reason_codes.append("NEW_DEVICE_ATO")
        if "recent_credential_modification" in signal_keys:
            reason_codes.append("CREDENTIAL_HIJACK")
        if "amount_drastically_exceeds_baseline" in signal_keys:
            reason_codes.append("HIGH_AMOUNT_ANOMALY")
        if "beneficiary_registered_moments_ago" in signal_keys or "limit_increased_immediately_prior" in signal_keys:
            reason_codes.append("RAPID_COERCION_PLAYBOOK")
        if "concurrent_active_voice_call" in signal_keys:
            reason_codes.append("ACTIVE_CALL_MANIPULATION")
        if "remote_screen_share_detected" in signal_keys:
            reason_codes.append("REMOTE_ACCESS_DETECTED")
        if "mtu_regulatory_cap_structuring" in signal_keys:
            reason_codes.append("MTU_CAP_STRUCTURING")
        if "first_time_destination_clabe" in signal_keys:
            reason_codes.append("NEW_DESTINATION_RISK")
        if "rapid_fan_in_destination_cluster" in signal_keys:
            reason_codes.append("FAN_IN_MULE_RISK")

        # 4. Apply Corroboration Decision Rules
        decision: str = "allow"

        # Hard safety override: remote screen share or active call + new destination = immediate pause
        if ("REMOTE_ACCESS_DETECTED" in reason_codes or "ACTIVE_CALL_MANIPULATION" in reason_codes) and "NEW_DESTINATION_RISK" in reason_codes:
            decision = "pause"
        elif elevated_count >= 3:
            decision = "pause"
        elif elevated_count == 2:
            # If two dimensions elevated and high amount (> $15,000 MXN) -> pause, else challenge
            if request.amount >= Decimal("15000.00"):
                decision = "pause"
            else:
                decision = "challenge"
        else:
            # 0 or 1 elevated dimension -> allow (prevents single-signal false alarms)
            decision = "allow"

        scores = ScoresBreakdown(
            ato=ato_score,
            intent=intent_score,
            recipient=recipient_score,
        )

        # 5. Generate Spanish explanation for the customer
        payer_message_es = default_explainer.explain(
            decision=decision,
            reason_codes=reason_codes,
            signals=all_signals,
        )

        return decision, scores, all_signals, reason_codes, payer_message_es
