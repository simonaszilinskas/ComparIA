"""add_user_profile_fields

Revision ID: e4a9c7f2b3d6
Revises: d1f4a2e7c9b5
Create Date: 2026-07-03 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

revision: str = 'e4a9c7f2b3d6'
down_revision: Union[str, Sequence[str], None] = 'd1f4a2e7c9b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'auth_user', sa.Column('profession', sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )
    op.add_column(
        'auth_user',
        sa.Column('ai_usage_frequency', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    )
    op.add_column(
        'auth_user', sa.Column('gender', sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )
    op.add_column(
        'auth_user', sa.Column('age_range', sqlmodel.sql.sqltypes.AutoString(), nullable=True)
    )


def downgrade() -> None:
    op.drop_column('auth_user', 'age_range')
    op.drop_column('auth_user', 'gender')
    op.drop_column('auth_user', 'ai_usage_frequency')
    op.drop_column('auth_user', 'profession')
