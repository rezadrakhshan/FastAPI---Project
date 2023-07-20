from db.datebase import Base
from sqlalchemy import String,Integer,Column

class User(Base):
    __tablename__ = "users"
    name = Column(String)
    password = Column(Integer)
    email = Column(String,primary_key=True)

