"""empty message

Revision ID: 95b31f3908b9
Revises: 
Create Date: 2018-01-30 17:05:40.665262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95b31f3908b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_categories_name'), 'categories', ['name'], unique=True)
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_roles_default'), 'roles', ['default'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('posts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('preview', sa.Text(), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('image_url', sa.String(length=125), nullable=True),
    sa.Column('body_html', sa.Text(), nullable=True),
    sa.Column('preview_html', sa.Text(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_posts_timestamp'), 'posts', ['timestamp'], unique=False)
    op.create_index(op.f('ix_posts_title'), 'posts', ['title'], unique=True)
    op.create_table('has_category',
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], ondelete='CASCADE')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('has_category')
    op.drop_index(op.f('ix_posts_title'), table_name='posts')
    op.drop_index(op.f('ix_posts_timestamp'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_roles_default'), table_name='roles')
    op.drop_table('roles')
    op.drop_index(op.f('ix_categories_name'), table_name='categories')
    op.drop_table('categories')
    # ### end Alembic commands ###
