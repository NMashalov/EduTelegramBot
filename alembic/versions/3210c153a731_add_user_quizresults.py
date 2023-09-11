"""add user quizResults

Revision ID: 3210c153a731
Revises: 0a9c9c3ea0bd
Create Date: 2023-09-11 01:02:12.885804

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3210c153a731'
down_revision: Union[str, None] = '0a9c9c3ea0bd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
