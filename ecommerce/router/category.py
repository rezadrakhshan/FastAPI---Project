from fastapi import APIRouter, File, UploadFile, Depends, Request
import os
from sqlalchemy.orm import Session
from db.datebase import get_db
from service import category
from router.user import templates
from db.models import *

router = APIRouter(
    tags=["category"]
)

@router.post("/category")
def create_category(
    name:str,
    db:Session = Depends(get_db)
    ):

    return category.add_category(
        name,
        db
    )

@router.get("/category/{category_name}")
def category_product(request:Request,category_name:str,db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.category == category_name)
    category = db.query(Category).all()
    listt = []
    for i in product:
        listt.append(i)
    if len(listt) == 0:
        return templates.TemplateResponse("404.html",{"request":request})
    else:
        return templates.TemplateResponse("category.html",{"request":request,"product":product,'category':category})