from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, backref, relation

db = create_engine('postgres://postgres:postgres@localhost:5432/pai', echo=False)

def get_session():
    return scoped_session(sessionmaker(autocommit=True,autoflush=True,bind=db))