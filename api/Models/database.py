from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = "root"
DB_PASSWORD = "fuwbYNrLduLeLciYpeMtjdbPmPMkAzoc"
DB_HOST = "autorack.proxy.rlwy.net"
DB_PORT = "40107"
DB_NAME = "railway"

engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()