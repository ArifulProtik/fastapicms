
from datetime import datetime
from sqlalchemy import Column, String, Boolean
import sqlalchemy
from sqlalchemy.sql.expression import true
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=true, index=true)
    name = Column(String)
    password = Column(String)
    is_active = Column(Boolean, default=True)
    profile_pic = Column(String)
    created = Column(sqlalchemy.DateTime, default=datetime.utcnow)


