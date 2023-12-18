"""initial migrate

Revision ID: 197e6c4ecabe
Revises: 
Create Date: 2023-12-19 05:07:00.264975

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "197e6c4ecabe"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "member",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False, unique=True),
        sa.Column("password", sa.String(length=255), nullable=False),
        sa.Column("token", sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["member.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "task",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("date", sa.String(length=255), nullable=True),
        sa.Column("status", sa.String(length=255), nullable=True),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["project_id"],
            ["project.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "task_member",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("member_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["member_id"],
            ["member.id"],
        ),
        sa.ForeignKeyConstraint(
            ["task_id"],
            ["task.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    op.create_table(
        "notif",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=False),
        sa.Column("date", sa.String(length=255), nullable=True),
        sa.Column("from_member_id", sa.Integer(), nullable=False),
        sa.Column("to_member_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["from_member_id"],
            ["member.id"],
        ),
        sa.ForeignKeyConstraint(
            ["to_member_id"],
            ["member.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("notif")
    op.drop_table("task_member")
    op.drop_table("task")
    op.drop_table("project")
    op.drop_table("member")
