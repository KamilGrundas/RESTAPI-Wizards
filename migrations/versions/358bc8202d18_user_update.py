"""user update

Revision ID: 358bc8202d18
Revises: b6d73bef9af6
Create Date: 2024-03-07 20:02:05.026520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '358bc8202d18'
down_revision: Union[str, None] = 'b6d73bef9af6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', sa.String(length=255), nullable=False))
    op.drop_column('users', 'mod')
    op.drop_column('users', 'standard_user')
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('standard_user', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('mod', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'role')
    # ### end Alembic commands ###
