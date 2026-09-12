"""Feature extraction layer computing behavioral baselines relative to simulated as_of time."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from decimal import Decimal
from typing import Any
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from sentinel.models import Event, Payer


def _to_utc(dt: datetime | None) -> datetime | None:
    """Normalize datetime to timezone-aware UTC."""
    if dt is None:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


@dataclass
class PayerFeatures:
    """Behavioral features and contextual baselines for a payer at a given moment."""

    payer_id: int
    as_of: datetime

    # 90-day baselines
    transfer_count_90d: int = 0
    max_amount_90d: Decimal = Decimal("0.00")
    avg_amount_90d: Decimal = Decimal("0.00")
    sum_amount_90d: Decimal = Decimal("0.00")
    usual_hours: set[int] = field(default_factory=set)
    known_beneficiary_clabes: set[str] = field(default_factory=set)
    known_institutions: set[str] = field(default_factory=set)
    known_devices: set[str] = field(default_factory=set)

    # Velocity and short-term windows
    velocity_1h_count: int = 0
    velocity_1h_amount: Decimal = Decimal("0.00")
    velocity_24h_count: int = 0
    velocity_24h_amount: Decimal = Decimal("0.00")

    # Destination relationship
    is_destination_clabe_known: bool = False
    is_destination_institution_known: bool = False
    beneficiary_created_minutes_ago: float | None = None

    # Limit and security lifecycle
    current_limit: Decimal | None = None
    limit_changed_minutes_ago: float | None = None
    limit_change_ratio: float | None = None
    credential_changed_hours_ago: float | None = None

    # Estimated balance
    last_known_balance: Decimal = Decimal("50000.00")


class FeatureStore:
    """Calculates payer features strictly relative to simulated as_of timestamp."""

    @staticmethod
    def get_features(
        db: Session,
        payer: Payer,
        destination_clabe: str,
        destination_institution_code: str,
        as_of: datetime,
    ) -> PayerFeatures:
        """Extract all baseline and velocity features as of the proposed transfer time."""
        as_of_utc = _to_utc(as_of)
        features = PayerFeatures(payer_id=payer.id, as_of=as_of_utc)

        window_90d_start = as_of_utc - timedelta(days=90)
        window_24h_start = as_of_utc - timedelta(hours=24)
        window_1h_start = as_of_utc - timedelta(hours=1)

        # 1. Fetch relevant events in the 90-day window strictly up to as_of
        stmt = (
            select(Event)
            .where(
                Event.payer_id == payer.id,
                Event.occurred_at <= as_of_utc,
                Event.occurred_at >= window_90d_start,
            )
            .order_by(Event.occurred_at.asc())
        )
        events = db.execute(stmt).scalars().all()

        amounts_90d: list[Decimal] = []
        clabes_seen: set[str] = set()
        institutions_seen: set[str] = set()
        devices_seen: set[str] = set()
        hours_seen: set[int] = set()

        v1h_count = 0
        v1h_amount = Decimal("0.00")
        v24h_count = 0
        v24h_amount = Decimal("0.00")

        latest_beneficiary_addition: datetime | None = None
        latest_limit_change: datetime | None = None
        latest_limit_val: Decimal | None = None
        previous_limit_val: Decimal | None = None
        latest_credential_change: datetime | None = None
        last_balance: Decimal | None = None

        for event in events:
            payload: dict[str, Any] = event.payload or {}
            event_type = event.type
            occ = _to_utc(event.occurred_at)

            if event_type == "transfer_settled":
                amt = Decimal(str(payload.get("amount", 0)))
                amounts_90d.append(amt)
                hours_seen.add(occ.hour)

                clabe = payload.get("destination_clabe")
                if clabe:
                    clabes_seen.add(clabe)
                inst = payload.get("destination_institution_code")
                if inst:
                    institutions_seen.add(inst)

                if occ >= window_24h_start:
                    v24h_count += 1
                    v24h_amount += amt
                if occ >= window_1h_start:
                    v1h_count += 1
                    v1h_amount += amt

                if "balance_after" in payload:
                    last_balance = Decimal(str(payload["balance_after"]))

            elif event_type == "beneficiary_added":
                clabe = payload.get("clabe") or payload.get("destination_clabe")
                if clabe and clabe == destination_clabe:
                    latest_beneficiary_addition = occ
                inst = payload.get("institution_code") or payload.get("destination_institution_code")
                # Do not treat newly added unverified institution as established prior history
                pass

            elif event_type == "limit_changed":
                latest_limit_change = occ
                if "new_limit" in payload:
                    previous_limit_val = latest_limit_val
                    latest_limit_val = Decimal(str(payload["new_limit"]))

            elif event_type == "credential_changed":
                latest_credential_change = occ

            elif event_type in ("session_started", "device_seen"):
                dev_id = payload.get("device_id")
                if dev_id:
                    devices_seen.add(dev_id)

        # Fill 90-day transfer statistics
        if amounts_90d:
            features.transfer_count_90d = len(amounts_90d)
            features.max_amount_90d = max(amounts_90d)
            features.sum_amount_90d = sum(amounts_90d)
            features.avg_amount_90d = features.sum_amount_90d / Decimal(len(amounts_90d))

        features.usual_hours = hours_seen
        features.known_beneficiary_clabes = clabes_seen
        features.known_institutions = institutions_seen
        features.known_devices = devices_seen

        features.velocity_1h_count = v1h_count
        features.velocity_1h_amount = v1h_amount
        features.velocity_24h_count = v24h_count
        features.velocity_24h_amount = v24h_amount

        # Destination flags
        features.is_destination_clabe_known = destination_clabe in clabes_seen
        features.is_destination_institution_known = destination_institution_code in institutions_seen

        if latest_beneficiary_addition:
            diff = (as_of_utc - latest_beneficiary_addition).total_seconds()
            features.beneficiary_created_minutes_ago = max(0.0, diff / 60.0)

        if latest_limit_change:
            diff = (as_of_utc - latest_limit_change).total_seconds()
            features.limit_changed_minutes_ago = max(0.0, diff / 60.0)
            features.current_limit = latest_limit_val
            if previous_limit_val and previous_limit_val > 0 and latest_limit_val:
                features.limit_change_ratio = float(latest_limit_val / previous_limit_val)

        if latest_credential_change:
            diff = (as_of_utc - latest_credential_change).total_seconds()
            features.credential_changed_hours_ago = max(0.0, diff / 3600.0)

        if last_balance is not None:
            features.last_known_balance = last_balance

        return features
