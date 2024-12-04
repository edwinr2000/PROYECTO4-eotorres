from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+mysqlconnector://root:fuwbYNrLduLeLciYpeMtjdbPmPMkAzoc@autorack.proxy.rlwy.net:40107/railway"

engine = create_engine(DB_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
