"""Initial migrations-new

Revision ID: 90292726be59
Revises: 
Create Date: 2024-09-10 00:00:40.652731

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90292726be59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event_categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('attendees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('organizers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=100), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('organizer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['event_categories.id'], ),
    sa.ForeignKeyConstraint(['organizer_id'], ['organizers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('rsvps',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('attendee_id', sa.Integer(), nullable=False),
    sa.Column('event_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attendee_id'], ['attendees.id'], ),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rsvps')
    op.drop_table('events')
    op.drop_table('organizers')
    op.drop_table('attendees')
    op.drop_table('users')
    op.drop_table('event_categories')
    # ### end Alembic commands ###
