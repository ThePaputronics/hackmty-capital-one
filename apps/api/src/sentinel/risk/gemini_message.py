"""Optional Gemini wording for a paused transfer; risk decisions remain rule-based."""

import json
import logging
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from sentinel.config import Settings

logger = logging.getLogger("sentinel")
MAX_MESSAGE_CHARS = 220

REASON_DESCRIPTIONS = {
    "ACTIVE_CALL_MANIPULATION": "an active phone call during the transfer",
    "REMOTE_ACCESS_DETECTED": "remote access or screen sharing",
    "RAPID_COERCION_PLAYBOOK": "a beneficiary or transfer limit changed shortly before the transfer",
    "NEW_DEVICE_ATO": "a new device",
    "CREDENTIAL_HIJACK": "recent account security changes",
    "HIGH_AMOUNT_ANOMALY": "an amount unusual for this account",
    "NEW_DESTINATION_RISK": "a new destination account",
    "MTU_CAP_STRUCTURING": "an amount near the transfer limit",
    "FAN_IN_MULE_RISK": "an unusual recipient activity pattern",
}


def generate_pause_message(reason_codes: list[str], settings: Settings) -> str | None:
    """Return concise Spanish guidance, or None when Gemini cannot provide it."""
    if not settings.gemini_api_key:
        return None

    reasons = [REASON_DESCRIPTIONS[code] for code in reason_codes if code in REASON_DESCRIPTIONS]
    prompt = (
        "Write a customer-facing message in Spanish (Mexico) for a bank transfer that has already "
        "been paused. Use only these detected factors: " + ", ".join(reasons or ["several corroborated risk factors"]) + ". "
        "Use one or two short sentences, at most 180 characters. State the pause and one safe next "
        "step, such as ending a call and contacting the bank through its official number. "
        "Be calm and clear. Do not claim fraud is certain, invent facts, include personal data, "
        "ask for credentials, or suggest transferring money. Return only the message text."
    )
    generation_config = {"temperature": 0.2, "maxOutputTokens": 256}
    if settings.gemini_model.startswith("gemini-2.5-flash"):
        generation_config["thinkingConfig"] = {"thinkingBudget": 0}
    elif settings.gemini_model.startswith(("gemini-3.5-flash", "gemini-3.6-flash")):
        generation_config["thinkingConfig"] = {"thinkingLevel": "minimal"}

    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": generation_config,
    }
    request = Request(
        f"https://generativelanguage.googleapis.com/v1beta/models/{settings.gemini_model}:generateContent",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "x-goog-api-key": settings.gemini_api_key},
        method="POST",
    )

    try:
        with urlopen(request, timeout=3) as response:
            result = json.load(response)
        parts = result["candidates"][0]["content"]["parts"]
        message = " ".join(part["text"] for part in parts if "text" in part).strip().strip('"“”')
        if not message or len(message) > MAX_MESSAGE_CHARS or "\n" in message:
            logger.warning("Gemini pause message was empty or exceeded the length limit")
            return None
        return message
    except (HTTPError, URLError, TimeoutError, OSError, ValueError, KeyError, IndexError, TypeError) as exc:
        logger.warning("Gemini pause message unavailable: %s", type(exc).__name__)
        return None
