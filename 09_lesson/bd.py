import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_connection = "postgresql://myuser:mypassword@localhost:5432/mydatabase"
db = create_engine(db_connection)


@pytest.fixture(scope="session")
def engine():
    return create_engine(db_connection)


@pytest.fixture
def session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker()(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
