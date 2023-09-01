from fastapi import Request, Depends, status,APIRouter
from fastapi.templating import Jinja2Templates
from db.database import get_db
from db.database import engine
from sqlalchemy.orm import Session
from db.models import Menu
from starlette.responses import RedirectResponse
from service import food


router = APIRouter()

@router.post('/add')
def add_food(
    name : str,
    detail : str,
    category:str,
    price : int,
    db : Session = Depends(get_db)
):
    return food.food(name,detail,category,price,db)

@router.delete("/delete")
def delete(
    slug:int,
    db:Session = Depends(get_db)
):
    item = db.query(Menu).filter(Menu.slug == slug).first()
    db.delete(item)
    db.commit()
    return "item deleted"
    