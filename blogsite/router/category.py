from fastapi import APIRouter , Depends , Response , Request
import os
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import Category,Blog
from router.home import templates
from service import category

router = APIRouter(
    tags=["categories"]
)

@router.post("/category")
def add_category(
    name:str, 
    db:Session = Depends(get_db)
):
    return category.create_category(name,db)

@router.delete("/delete/category")
def delete_category(
    slug:int,
    db : Session = Depends(get_db)
):
    item = db.query(Category).filter(Category.slug == slug).first()
    db.delete(item)
    db.commit()


@router.get("/category/{category_name}")
def category(
    request:Request,
    category_name:str,
    db : Session = Depends(get_db)
):
    category_item = db.query(Blog).filter(Blog.category == category_name)
    return templates.TemplateResponse("category.html",{"request":request,"category_item":category_item})
