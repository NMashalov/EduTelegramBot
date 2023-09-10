"""pls

Revision ID: 632395367d26
Revises: c90af8d2bef3
Create Date: 2023-09-10 23:31:48.209966

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '632395367d26'
down_revision: Union[str, None] = 'c90af8d2bef3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
