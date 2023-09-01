from db.database import Base
from sqlalchemy import String,Integer,Column

class Menu(Base):
    __tablename__ = "foods"
    name = Column(String)
    detail = Column(String)
    category = Column(String)
    price = Column(Integer)
    slug = Column(Integer,primary_key=True,index=True)


class Message(Base):
    __tablename__ = "Messages"
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    message = Column(String)
    slug = Column(Integer,primary_key=True,index=True)
