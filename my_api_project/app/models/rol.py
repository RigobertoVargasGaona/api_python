# app/models/user.py

from sqlalchemy import Column, Integer, String
from app.config.db import Base

class Rol(Base):
    __tablename__ = "roles"
    rol_id = Column(Integer, primary_key=True, index=True)
    rol_name = Column(String(50), unique=True, nullable=False)
