from sqlalchemy import Column, Integer, String, Boolean
from flask_login import UserMixin
from .database import Base

class User(UserMixin, Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    es_admin = Column(Boolean, default=False)
    es_empleado = Column(Boolean, default=False)
