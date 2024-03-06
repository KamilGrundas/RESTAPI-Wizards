"""picture update

Revision ID: 24282a464010
Revises: 99a680a161a1
Create Date: 2024-03-06 16:50:34.607754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '24282a464010'
down_revision: Union[str, None] = '99a680a161a1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pictures', sa.Column('description', sa.String(length=300), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('pictures', 'description')
    # ### end Alembic commands ###
