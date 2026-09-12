"""Synthetic personas and scam playbooks."""

from dataclasses import dataclass, field
from datetime import datetime, timedelta
import random
from typing import Any, Literal


@dataclass
class BeneficiaryProfile:
    """Pre-established or dynamically added beneficiary."""

    clabe: str
    institution_code: str
    alias: str
    created_at: datetime


@dataclass
class Persona:
    """Base class for synthetic financial actors."""

    external_id: str
    institution_code: str
    persona_type: Literal["normal", "merchant", "victim", "ato"]
    device_id: str
    usual_balance: float = 35000.0
    current_balance: float = 35000.0
    known_beneficiaries: list[BeneficiaryProfile] = field(default_factory=list)
    daily_limit: float = 20000.0


def generate_valid_clabe(inst_code: str, account_num: str) -> str:
    """Generate a valid 18-digit CLABE with ABM check digit."""
    # 3 digit bank + 3 digit plaza + 11 digit account
    plaza = "180"  # CDMX standard plaza
    inst = inst_code.zfill(3)
    acc = account_num.zfill(11)
    base17 = f"{inst}{plaza}{acc}"

    # ABM check digit calculation (weights: 3, 7, 1 repeating)
    weights = [3, 7, 1] * 5 + [3, 7]
    weighted_sum = sum(int(digit) * weight for digit, weight in zip(base17, weights))
    check_digit = (10 - (weighted_sum % 10)) % 10
    return f"{base17}{check_digit}"


class PersonaFactory:
    """Creates diverse cohorts of financial actors."""

    INSTITUTIONS = ["012", "002", "014", "072", "127", "021", "137"]  # BBVA, Banamex, Santander, Banorte, Azteca, HSBC, BanCoppel

    @classmethod
    def create_normal_payer(cls, idx: int, created_at: datetime) -> Persona:
        """Create a typical consumer with regular household payment habits."""
        p_id = f"payer_normal_{idx:03d}"
        inst = random.choice(cls.INSTITUTIONS)
        dev = f"dev_{p_id}"
        persona = Persona(
            external_id=p_id,
            institution_code=inst,
            persona_type="normal",
            device_id=dev,
            usual_balance=random.uniform(15000, 60000),
        )
        persona.current_balance = persona.usual_balance

        # Add 2 to 4 habitual beneficiaries
        for b_idx in range(random.randint(2, 4)):
            dest_inst = random.choice(cls.INSTITUTIONS)
            clabe = generate_valid_clabe(dest_inst, f"{idx:03d}{b_idx:02d}000000")
            persona.known_beneficiaries.append(
                BeneficiaryProfile(
                    clabe=clabe,
                    institution_code=dest_inst,
                    alias=f"Contacto {b_idx + 1}",
                    created_at=created_at - timedelta(days=random.randint(30, 85)),
                )
            )
        return persona

    @classmethod
    def create_small_merchant(cls, idx: int, created_at: datetime) -> Persona:
        """Create a small merchant (taqueria, gym, grocery) with legitimate frequent cash flow."""
        p_id = f"merchant_pyme_{idx:03d}"
        inst = random.choice(cls.INSTITUTIONS)
        dev = f"dev_pos_{p_id}"
        persona = Persona(
            external_id=p_id,
            institution_code=inst,
            persona_type="merchant",
            device_id=dev,
            usual_balance=random.uniform(50000, 180000),
            daily_limit=100000.0,
        )
        persona.current_balance = persona.usual_balance

        # 6 to 10 regular suppliers and employees
        for b_idx in range(random.randint(6, 10)):
            dest_inst = random.choice(cls.INSTITUTIONS)
            clabe = generate_valid_clabe(dest_inst, f"9{idx:02d}{b_idx:02d}000000")
            persona.known_beneficiaries.append(
                BeneficiaryProfile(
                    clabe=clabe,
                    institution_code=dest_inst,
                    alias=f"Proveedor {b_idx + 1}",
                    created_at=created_at - timedelta(days=random.randint(45, 89)),
                )
            )
        return persona

    @classmethod
    def create_vulnerable_victim(cls, idx: int, created_at: datetime) -> Persona:
        """Create a consumer destined to be targeted by a coercion scam playbook."""
        p_id = f"victim_target_{idx:03d}"
        inst = random.choice(cls.INSTITUTIONS)
        dev = f"dev_phone_{p_id}"
        persona = Persona(
            external_id=p_id,
            institution_code=inst,
            persona_type="victim",
            device_id=dev,
            usual_balance=random.uniform(20000, 75000),
            daily_limit=15000.0,
        )
        persona.current_balance = persona.usual_balance

        # 2 family contacts
        for b_idx in range(2):
            dest_inst = random.choice(cls.INSTITUTIONS)
            clabe = generate_valid_clabe(dest_inst, f"7{idx:02d}{b_idx:02d}000000")
            persona.known_beneficiaries.append(
                BeneficiaryProfile(
                    clabe=clabe,
                    institution_code=dest_inst,
                    alias=f"Familiar {b_idx + 1}",
                    created_at=created_at - timedelta(days=random.randint(30, 80)),
                )
            )
        return persona

    @classmethod
    def create_ato_target(cls, idx: int, created_at: datetime) -> Persona:
        """Create a profile targeted for credential takeover from an unknown device."""
        p_id = f"ato_target_{idx:03d}"
        inst = random.choice(cls.INSTITUTIONS)
        dev = f"dev_genuine_{p_id}"
        persona = Persona(
            external_id=p_id,
            institution_code=inst,
            persona_type="ato",
            device_id=dev,
            usual_balance=random.uniform(30000, 90000),
        )
        persona.current_balance = persona.usual_balance
        dest_inst = random.choice(cls.INSTITUTIONS)
        persona.known_beneficiaries.append(
            BeneficiaryProfile(
                clabe=generate_valid_clabe(dest_inst, f"5{idx:02d}01000000"),
                institution_code=dest_inst,
                alias="Ahorro Personal",
                created_at=created_at - timedelta(days=60),
            )
        )
        return persona
