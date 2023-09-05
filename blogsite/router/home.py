from fastapi import Request, Depends, status,APIRouter
from fastapi.templating import Jinja2Templates
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import Category,Blog

router = APIRouter(
    tags=['home']
)

templates = Jinja2Templates(directory="templates")

@router.get("/")
def home(
    request:Request,
    db : Session = Depends(get_db)
):
    category = db.query(Category).all()
    blogs = db.query(Blog).all()
    return templates.TemplateResponse("index.html",{"request":request,"category":category,"blogs":blogs})


@router.get("/{slug}")
def detail(
    slug:int,
    request:Request,
    db:Session = Depends(get_db)
):
    item = db.query(Blog).filter(Blog.slug == slug).first()
    return templates.TemplateResponse("detail.html",{"request":request,"item":item})

@router.get("/author/{author_name}")
def author(
    request:Request,
    author_name:str,
    db:Session = Depends(get_db)
):
    author = db.query(Blog).filter(Blog.author == author_name)
    return templates.TemplateResponse("author.html",{"request":request,"author":author})