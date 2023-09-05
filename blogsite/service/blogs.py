from sqlalchemy.orm import Session
from db.models import Blog

def add_blog(
        title:str,
        text:str,
        date:str,
        author:str,
        category:str,
        filepath:str,
        db:Session
):
    new_blog = Blog(
        title = title,
        text = text,
        date = date,
        author = author,
        category = category,
        image = filepath
    )
    db.add(new_blog)
    db.commit()
    return new_blog