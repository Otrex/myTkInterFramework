from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.Settings import DB_HOST


Base = declarative_base()
engine = create_engine(DB_HOST)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base.query = db_session.query_property()

def create_all():
	Base.metadata.create_all(engine)
	engine.connect()

