"""create tables

Revision ID: 5f16b46f8f6f
Revises: 46747276044f
Create Date: 2023-09-10 13:11:44.431725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f16b46f8f6f'
down_revision: Union[str, None] = '46747276044f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
