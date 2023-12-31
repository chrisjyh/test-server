from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "mysql+pymysql://root:1234@127.0.0.1:3307/todos"

engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionFactory()
session.query()


def get_db():
    sesson = SessionFactory()

    try:
        yield session
    finally:
        session.close()
