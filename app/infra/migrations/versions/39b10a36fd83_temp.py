"""Temp

Revision ID: 39b10a36fd83
Revises: 599a3d4bdd57
Create Date: 2024-10-02 08:49:31.050835

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '39b10a36fd83'
down_revision: Union[str, None] = '599a3d4bdd57'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Breed', 'id',
               existing_type=sa.UUID(),
               nullable=False,
               existing_server_default=sa.text('gen_random_uuid()'))
    op.alter_column('Cat', 'id',
               existing_type=sa.UUID(),
               nullable=False,
               existing_server_default=sa.text('gen_random_uuid()'))
    op.alter_column('Cat', 'breed_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.create_foreign_key(None, 'Cat', 'Breed', ['breed_id'], ['id'], ondelete='cascade')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Cat', type_='foreignkey')
    op.alter_column('Cat', 'breed_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('Cat', 'id',
               existing_type=sa.UUID(),
               nullable=True,
               existing_server_default=sa.text('gen_random_uuid()'))
    op.alter_column('Breed', 'id',
               existing_type=sa.UUID(),
               nullable=True,
               existing_server_default=sa.text('gen_random_uuid()'))
    # ### end Alembic commands ###
