from fastapi import APIRouter, File, UploadFile, Depends, Request
import os
from router.user import templates
from sqlalchemy.orm import Session
from db.datebase import get_db
from db.models import Blog
from datetime import datetime
from service import blogs as vv


router = APIRouter(
    tags=["blogs"]
)

@router.get("/create")
def add_blog(
    title:str,
    description:str,
    date_created:str | None = None,
    db:Session = Depends(get_db)
):
    return vv.add_blog(
        title,
        description,
        date_created,
        db
    )

@router.get("/allblogs")
def blogs(
    request:Request,
    db:Session = Depends(get_db)
):
    blogs = db.query(Blog).all()
    return templates.TemplateResponse("blog.html",{"request":request,"blogs":blogs})

@router.get("/blog/{blog_id}")
def detail(
    request:Request,
    blog_id:int,
    db : Session = Depends(get_db)
):
    item = db.query(Blog).filter(Blog.id == blog_id).first()
    return templates.TemplateResponse("detail.html",{"request":request,"item":item})