from sqlalchemy.orm import Session
from db.models import Blog
from datetime import datetime


def add_blog(
    title:str,
    description:str,
    date_created:str,
    db:Session
):
    new_blog = Blog(
        title = title,
        description = description,
        date_created = date_created
    )
    db.add(new_blog)
    db.commit()
