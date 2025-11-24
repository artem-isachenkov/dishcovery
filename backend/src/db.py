from sqlmodel import MetaData, SQLModel, Session, create_engine
from sqlalchemy.orm import configure_mappers
import config

DATABASE_URL = config.DATABASE_URL
engine = create_engine(DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    configure_mappers()


# metadata = MetaData()

# # Reflect the 'users' table from the 'auth' schema
# metadata.reflect(bind=engine, schema="auth")
# users_table = metadata.tables["auth.users"]

# # Print the columns in the 'users' table to check the field names
# print("user columns", users_table.columns.keys()) 