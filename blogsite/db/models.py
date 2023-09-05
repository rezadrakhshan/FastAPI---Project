from db.database import Base
from sqlalchemy import String,Integer,Column


class Category(Base):
    __tablename__ = "categories"
    name = Column(String)
    slug = Column(Integer,primary_key=True,index=True)

class Blog(Base):
    __tablename__ = "blogs"
    title = Column(String)
    text = Column(String)
    date = Column(String)
    author = Column(String)
    category = Column(String)
    image = Column(String)
    slug = Column(Integer,primary_key=True,index=True)