"""'Init'

Revision ID: 8079761326af
Revises: 
Create Date: 2024-03-09 11:30:42.808021

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8079761326af'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=250), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('crated_at', sa.DateTime(), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.Column('role', sa.String(length=255), nullable=False),
    sa.Column('is_banned', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('pictures',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('public_id', sa.String(length=255), nullable=True),
    sa.Column('url', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('picture_id', sa.Integer(), nullable=False),
    sa.Column('picture_comment_id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=200), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('edited_at', sa.DateTime(), nullable=True),
    sa.Column('is_deleted', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('picture_id', 'picture_comment_id'),
    sa.UniqueConstraint('picture_id', 'picture_comment_id', name='unique_pair_picture_comment')
    )
    op.create_table('picture_m2m_tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('picture_id', sa.Integer(), nullable=True),
    sa.Column('tag_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transformed_pictures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('picture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['picture_id'], ['pictures.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transformed_pictures_id'), 'transformed_pictures', ['id'], unique=False)
    op.create_table('qrcodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(), nullable=True),
    sa.Column('transformed_picture_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transformed_picture_id'], ['transformed_pictures.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_qrcodes_id'), 'qrcodes', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_qrcodes_id'), table_name='qrcodes')
    op.drop_table('qrcodes')
    op.drop_index(op.f('ix_transformed_pictures_id'), table_name='transformed_pictures')
    op.drop_table('transformed_pictures')
    op.drop_table('picture_m2m_tag')
    op.drop_table('comments')
    op.drop_table('pictures')
    op.drop_table('users')
    op.drop_table('tags')
    # ### end Alembic commands ###