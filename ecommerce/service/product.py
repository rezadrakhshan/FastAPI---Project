from sqlalchemy.orm import Session
from db.models import Product

def add_product(
    price:float,
    name:str,
    category:str,
    gender:str,
    detail:str,
    filepath:str,
    db:Session,
):
    new_product = Product(
        price = price,
        name = name,
        category = category,
        gender = gender,
        detail = detail,
        image = filepath,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    
    return new_product