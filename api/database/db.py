from sqlalchemy.orm import declarative_base
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(config.DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()


def get_db():
    with SessionLocal() as db:
        yield db
