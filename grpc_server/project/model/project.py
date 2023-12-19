from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

# op.create_table(
#     "project",
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("title", sa.String(length=255), nullable=False),
#     sa.Column("description", sa.Text(), nullable=True),
#     sa.Column("user_id", sa.Integer(), nullable=False),
#     sa.ForeignKeyConstraint(
#         ["user_id"],
#         ["member.id"],
#     ),
#     sa.PrimaryKeyConstraint("id"),
# )


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    user_id = Column(Integer, nullable=False)
