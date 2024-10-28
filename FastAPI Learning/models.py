from sqlalchemy import Column, Integer, String
from user_table.database import Base  # Correctly importing Base from database.py

# SQLAlchemy Users model
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100))
    password = Column(String(200))
