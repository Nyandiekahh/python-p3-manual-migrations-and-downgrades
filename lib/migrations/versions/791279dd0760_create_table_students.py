# migrations/versions/791279dd0760_create_table_students.py
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '791279dd0760'
down_revision = '6b9cb35ba46e'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table('students',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(length=55), nullable=True),
        sa.Column('grade', sa.Integer(), nullable=True),
        sa.Column('birthday', sa.DateTime(), nullable=True),
        sa.Column('enrolled_date', sa.DateTime(), nullable=True),
        sa.CheckConstraint('grade BETWEEN 1 AND 12', name='grade_between_1_and_12'),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email', name='unique_email')
    )
    op.create_index(op.f('ix_students_name'), 'students', ['name'], unique=False)

def downgrade() -> None:
    op.drop_index(op.f('ix_students_name'), table_name='students')
    op.drop_table('students')
