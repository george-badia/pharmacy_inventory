"""customers seede secsesfuly

Revision ID: c6d46cc304aa
Revises: 415c42f463fe
Create Date: 2024-09-19 02:21:34.671797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6d46cc304aa'
down_revision: Union[str, None] = '415c42f463fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
