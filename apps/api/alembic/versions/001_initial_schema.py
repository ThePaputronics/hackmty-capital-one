"""Initial schema for Sentinel API

Revision ID: 001_initial_schema
Revises:
Create Date: 2026-09-12 06:40:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = "001_initial_schema"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # 1. Payers table
    op.create_table(
        "payers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("external_id", sa.String(length=100), nullable=False),
        sa.Column("institution_code", sa.String(length=40), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_payers_id", "payers", ["id"], unique=False)
    op.create_index("ix_payers_external_id", "payers", ["external_id"], unique=True)
    op.create_index("ix_payers_institution_code", "payers", ["institution_code"], unique=False)

    # 2. Events table (append-only ledger)
    op.create_table(
        "events",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("payer_id", sa.Integer(), nullable=False),
        sa.Column("type", sa.String(length=80), nullable=False),
        sa.Column("occurred_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("payload", sa.JSON(), nullable=False),
        sa.ForeignKeyConstraint(["payer_id"], ["payers.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_events_id", "events", ["id"], unique=False)
    op.create_index("ix_events_payer_id", "events", ["payer_id"], unique=False)
    op.create_index("ix_events_type", "events", ["type"], unique=False)
    op.create_index("ix_events_occurred_at", "events", ["occurred_at"], unique=False)
    op.create_index("idx_events_payer_occurred", "events", ["payer_id", "occurred_at"], unique=False)
    op.create_index("idx_events_type_occurred", "events", ["type", "occurred_at"], unique=False)

    # 3. Evaluations table
    op.create_table(
        "evaluations",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("payer_id", sa.Integer(), nullable=False),
        sa.Column("destination_clabe", sa.String(length=30), nullable=False),
        sa.Column("destination_institution_code", sa.String(length=40), nullable=False),
        sa.Column("amount", sa.Numeric(precision=18, scale=2), nullable=False),
        sa.Column("currency", sa.String(length=3), nullable=False, server_default="MXN"),
        sa.Column("proposed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("decision", sa.String(length=20), nullable=False),
        sa.Column("score_ato", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("score_intent", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("score_recipient", sa.Numeric(precision=5, scale=4), nullable=False),
        sa.Column("reason_codes", sa.JSON(), nullable=False),
        sa.Column("payer_message_es", sa.Text(), nullable=False),
        sa.Column("latency_ms", sa.Integer(), nullable=False, server_default="0"),
        sa.Column("ruleset_version", sa.String(length=50), nullable=False),
        sa.Column("evaluated_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.ForeignKeyConstraint(["payer_id"], ["payers.id"], ondelete="RESTRICT"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_evaluations_id", "evaluations", ["id"], unique=False)
    op.create_index("ix_evaluations_payer_id", "evaluations", ["payer_id"], unique=False)
    op.create_index("ix_evaluations_destination_clabe", "evaluations", ["destination_clabe"], unique=False)
    op.create_index("ix_evaluations_decision", "evaluations", ["decision"], unique=False)
    op.create_index("ix_evaluations_proposed_at", "evaluations", ["proposed_at"], unique=False)

    # 4. Evaluation Signals table
    op.create_table(
        "evaluation_signals",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("evaluation_id", sa.Integer(), nullable=False),
        sa.Column("key", sa.String(length=100), nullable=False),
        sa.Column("signal_group", sa.String(length=40), nullable=False),
        sa.Column("points", sa.Integer(), nullable=False),
        sa.Column("observed", sa.String(length=255), nullable=False),
        sa.Column("baseline", sa.String(length=255), nullable=False),
        sa.Column("explanation", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(["evaluation_id"], ["evaluations.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_evaluation_signals_id", "evaluation_signals", ["id"], unique=False)
    op.create_index("ix_evaluation_signals_evaluation_id", "evaluation_signals", ["evaluation_id"], unique=False)

    # 5. Outcomes table
    op.create_table(
        "outcomes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("evaluation_id", sa.Integer(), nullable=False),
        sa.Column("outcome", sa.String(length=40), nullable=False),
        sa.Column("reported_at", sa.DateTime(timezone=True), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=False),
        sa.ForeignKeyConstraint(["evaluation_id"], ["evaluations.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_outcomes_id", "outcomes", ["id"], unique=False)
    op.create_index("ix_outcomes_evaluation_id", "outcomes", ["evaluation_id"], unique=True)


def downgrade() -> None:
    op.drop_table("outcomes")
    op.drop_table("evaluation_signals")
    op.drop_table("evaluations")
    op.drop_table("events")
    op.drop_table("payers")
