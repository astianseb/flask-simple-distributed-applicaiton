from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
import re

uri = os.environ.get('DATABASE_URL', 'postgres://sguser:sgpass@10.0.1.21/flaskdb')
#uri = os.environ.get('DATABASE_URL', 'postgres://sguser:sgpass@127.0.0.1/flaskdb')

engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
					 autoflush=False,
					 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def check_db_type():
    ip_add = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", uri)
    if str(ip_add[0]) == "127.0.0.1":
        return "local"
    else:
        return "remote"

db_type = check_db_type()

def init_db():
  import Flasktest.models
  Base.metadata.create_all(bind=engine)
