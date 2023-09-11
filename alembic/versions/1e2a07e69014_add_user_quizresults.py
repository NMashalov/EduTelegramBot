"""add user quizResults

Revision ID: 1e2a07e69014
Revises: 3210c153a731
Create Date: 2023-09-11 01:02:49.932137

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e2a07e69014'
down_revision: Union[str, None] = '3210c153a731'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
