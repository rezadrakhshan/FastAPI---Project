from sqlalchemy.orm import Session
from db.models import Category



def add_category(
    name:str,
    db:Session
):
    new_category = Category(
        name=name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)

    return new_category
