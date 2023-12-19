from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .meta import Base


# op.create_table(
#     "task",
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=255), nullable=False),
#     sa.Column("description", sa.Text(), nullable=True),
#     sa.Column("date", sa.String(length=255), nullable=True),
#     sa.Column("status", sa.String(length=255), nullable=True),
#     sa.Column("project_id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["project_id"],
#         ["project.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    date = Column(String(255), nullable=True)
    status = Column(String(255), nullable=True)
    project_id = Column(Integer, nullable=False)
    # project = relationship("Project", backref="task")
    # task_member = relationship("TaskMember", backref="task")
