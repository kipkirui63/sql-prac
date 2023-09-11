"""create tables

Revision ID: 92a99091f5ba
Revises: 5f16b46f8f6f
Create Date: 2023-09-10 13:14:52.417685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '92a99091f5ba'
down_revision: Union[str, None] = '5f16b46f8f6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
