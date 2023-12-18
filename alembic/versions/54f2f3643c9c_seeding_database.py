"""seeding database

Revision ID: 54f2f3643c9c
Revises: 197e6c4ecabe
Create Date: 2023-12-19 05:18:56.856076

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "54f2f3643c9c"
down_revision: Union[str, None] = "197e6c4ecabe"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        sa.table(
            "member",
            sa.column("name", sa.String(length=255)),
            sa.column("email", sa.String(length=255)),
            sa.column("password", sa.String(length=255)),
        ),
        [
            {
                "name": "maybeenang",
                "email": "maybeenang@dev.com",
                "password": "12345678",
            },
            {
                "name": "mab",
                "email": "mab@email.com",
                "password": "12345678",
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "project",
            sa.column("title", sa.String(length=255)),
            sa.column("description", sa.Text()),
            sa.column("user_id", sa.Integer()),
        ),
        [
            {
                "title": "project 1",
                "description": "project 1 description",
                "user_id": 1,
            },
            {
                "title": "project 2",
                "description": "project 2 description",
                "user_id": 2,
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "task",
            sa.column("title", sa.String(length=255)),
            sa.column("description", sa.Text()),
            sa.column("date", sa.String(length=255)),
            sa.column("status", sa.String(length=255)),
            sa.column("project_id", sa.Integer()),
        ),
        [
            {
                "title": "task 1",
                "description": "task 1 description",
                "date": "2021-12-19",
                "status": "todo",
                "project_id": 1,
            },
            {
                "title": "task 2",
                "description": "task 2 description",
                "date": "2021-12-19",
                "status": "todo",
                "project_id": 2,
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "task_member",
            sa.column("task_id", sa.Integer()),
            sa.column("member_id", sa.Integer()),
        ),
        [
            {
                "task_id": 1,
                "member_id": 1,
            },
            {
                "task_id": 2,
                "member_id": 2,
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "notif",
            sa.column("description", sa.String(length=255)),
            sa.column("date", sa.String(length=255)),
            sa.column("from_member_id", sa.Integer()),
            sa.column("to_member_id", sa.Integer()),
        ),
        [
            {
                "description": "notif 1",
                "date": "2021-12-19",
                "from_member_id": 1,
                "to_member_id": 2,
            },
            {
                "description": "notif 2",
                "date": "2021-12-19",
                "from_member_id": 2,
                "to_member_id": 1,
            },
        ],
    )


def downgrade() -> None:
    op.execute("TRUNCATE TABLE member")
    op.execute("TRUNCATE TABLE project")
    op.execute("TRUNCATE TABLE task")
    op.execute("TRUNCATE TABLE task_member")
    op.execute("TRUNCATE TABLE notif")
