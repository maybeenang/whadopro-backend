from sqlalchemy import Column, Integer, Text, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from .meta import Base

# op.create_table(
#     "member",
#     sa.Column("id", sa.Integer(), nullable=False),
#     sa.Column("name", sa.String(length=255), nullable=False),
#     sa.Column("email", sa.String(length=255), nullable=False, unique=True),
#     sa.Column("password", sa.String(length=255), nullable=False),
#     sa.Column("token", sa.String(length=255), nullable=True),
#     sa.PrimaryKeyConstraint("id"),
# )


class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    token = Column(String(255), nullable=True)
