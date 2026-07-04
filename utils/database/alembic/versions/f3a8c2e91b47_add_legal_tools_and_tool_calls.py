"""add legal tools/skills selection and tool_calls audit

Revision ID: f3a8c2e91b47
Revises: a1c3e5f7b9d2
Create Date: 2026-07-04 00:00:00.000000

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

# revision identifiers, used by Alembic.
revision: str = "f3a8c2e91b47"
down_revision: Union[str, Sequence[str], None] = "a1c3e5f7b9d2"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "comparison", sa.Column("enabled_skills", JSONB(), nullable=True)
    )
    op.add_column(
        "comparison", sa.Column("enabled_mcp_servers", JSONB(), nullable=True)
    )
    op.add_column(
        "llm_message", sa.Column("tool_calls", JSONB(), nullable=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("llm_message", "tool_calls")
    op.drop_column("comparison", "enabled_mcp_servers")
    op.drop_column("comparison", "enabled_skills")
