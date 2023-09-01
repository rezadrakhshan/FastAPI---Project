from sqlalchemy.orm import Session
from db.models import Menu 

def food(
        name:str,
        detail:str,
        category:str,
        price:int,
        db:Session
):
    new_food = Menu(
        name = name,
        detail = detail,
        category = category,
        price = price
    )
    db.add(new_food)
    db.commit()
    db.refresh(new_food)
    return new_food