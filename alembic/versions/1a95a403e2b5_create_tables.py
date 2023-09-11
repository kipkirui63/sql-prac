"""create tables

Revision ID: 1a95a403e2b5
Revises: 92a99091f5ba
Create Date: 2023-09-10 13:30:40.849958

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a95a403e2b5'
down_revision: Union[str, None] = '92a99091f5ba'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
