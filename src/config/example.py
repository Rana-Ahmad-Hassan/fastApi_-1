from sqlmodel import SQLModel, Session, create_engine
import os

connection_str = "postgresql+asyncpg://neondb_owner:npg_M5zP2EVFbSqh@ep-nameless-truth-a4d27dsm-pooler.us-east-1.aws.neon.tech/neondb"
print(connection_str)
engine = create_engine(connection_str)


def get_session():
    with Session(engine) as session:
        yield session


def create_tables():
    SQLModel.metadata.create_all(engine)
