"""medication seeded succsesfully

Revision ID: eaaaf11932d4
Revises: c6d46cc304aa
Create Date: 2024-09-19 02:25:14.418928

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eaaaf11932d4'
down_revision: Union[str, None] = 'c6d46cc304aa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
