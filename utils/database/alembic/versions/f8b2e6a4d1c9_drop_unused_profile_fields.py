"""drop_unused_profile_fields

Revision ID: f8b2e6a4d1c9
Revises: e4a9c7f2b3d6
Create Date: 2026-07-04 00:00:00.000000

"""
from typing import Sequence, Union

import sqlalchemy as sa
import sqlmodel
from alembic import op

revision: str = 'f8b2e6a4d1c9'
down_revision: Union[str, Sequence[str], None] = 'e4a9c7f2b3d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('auth_user', 'age_range')
    op.drop_column('auth_user', 'gender')
    op.drop_column('auth_user', 'ai_usage_frequency')


def downgrade() -> None:
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
