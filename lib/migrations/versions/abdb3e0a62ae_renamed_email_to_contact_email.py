# migrations/versions/abdb3e0a62ae_renamed_email_to_contact_email.py
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'abdb3e0a62ae'
down_revision = '791279dd0760'  # This should be correct if the previous migration is '791279dd0760'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.alter_column('students', 'email', new_column_name='contact_email')

def downgrade() -> None:
    op.alter_column('students', 'contact_email', new_column_name='email')
