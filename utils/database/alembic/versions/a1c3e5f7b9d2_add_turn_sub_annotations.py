"""add_turn_sub_annotations

Revision ID: a1c3e5f7b9d2
Revises: f8b2e6a4d1c9
Create Date: 2026-07-04 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import JSONB

revision: str = 'a1c3e5f7b9d2'
down_revision: Union[str, Sequence[str], None] = 'f8b2e6a4d1c9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'turn',
        sa.Column('sub_annotations_a', JSONB(), nullable=False, server_default='[]'),
    )
    op.add_column(
        'turn',
        sa.Column('sub_annotations_b', JSONB(), nullable=False, server_default='[]'),
    )


def downgrade() -> None:
    op.drop_column('turn', 'sub_annotations_b')
    op.drop_column('turn', 'sub_annotations_a')
