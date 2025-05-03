from sqlmodel import SQLModel, Field, Column
import uuid
import sqlalchemy.dialects.postgresql as pg
from datetime import datetime


class Book(SQLModel, table=True):  # Ensure table creation
    __tablename__ = 'books'  # Optional but explicit

    id: uuid.UUID = Field(
        default_factory=uuid.uuid4,
        sa_column=Column(
            pg.UUID(as_uuid=True),
            primary_key=True,
            nullable=False,
            default=uuid.uuid4
        )
    )

    title: str = Field(
        min_length=1,
        max_length=255,
        sa_column=Column(pg.TEXT, nullable=False)
    )

    author: str = Field(
        min_length=1,
        max_length=255,
        sa_column=Column(pg.TEXT, nullable=False)
    )

    publisher: str = Field(
        min_length=1,
        max_length=255,
        sa_column=Column(pg.TEXT, nullable=False)
    )

    publish_date: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False)
    )

    page_count: int = Field(
        ge=1,
        sa_column=Column(pg.INTEGER, nullable=False)
    )

    created_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            pg.TIMESTAMP,
            nullable=False,
            default=datetime.now
        )
    )

    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column=Column(
            pg.TIMESTAMP,
            nullable=False,
            default=datetime.now,
        )
    )


def __repr__(self) -> str:
    return f"<Book(id={self.id}, title={self.title}, author={self.author})>"