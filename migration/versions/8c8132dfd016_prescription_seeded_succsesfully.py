"""prescription seeded succsesfully

Revision ID: 8c8132dfd016
Revises: eaaaf11932d4
Create Date: 2024-09-19 02:27:00.806997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c8132dfd016'
down_revision: Union[str, None] = 'eaaaf11932d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
