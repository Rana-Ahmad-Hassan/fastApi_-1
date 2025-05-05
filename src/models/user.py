from sqlmodel import SQLModel, Field, Column
import uuid
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )

    username: str = Field(
        min_length=3,
        max_length=30,
        sa_column=Column(pg.VARCHAR(30), unique=True, nullable=False)
    )

    password: str = Field(
        min_length=3,
        max_length=128,
        sa_column=Column(pg.VARCHAR(128), nullable=False)
    )

    email: str = Field(
        min_length=3,
        max_length=100,
        sa_column=Column(pg.VARCHAR(100), unique=True, nullable=False)
    )

    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            default=datetime.now
        )
    )

    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            pg.TIMESTAMP(timezone=True),
            nullable=False,
            default=datetime.now,
            onupdate=datetime.now
        )
    )

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
