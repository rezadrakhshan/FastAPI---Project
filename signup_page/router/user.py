from fastapi import APIRouter, Depends, Request, Form, status
from db.datebase import get_db
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from service import user
from starlette.responses import RedirectResponse




router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/home")
def home(request:Request):
    return templates.TemplateResponse("home.html",{"request":request})


@router.get("/")
def signup(request:Request):
    return templates.TemplateResponse("index.html",{"request":request})

@router.post("/add")
def add_user(
    username : str = Form(media_type="application/x-www-form-urlencoded"),
    email : str = Form(media_type="application/x-www-form-urlencoded"),
    password : int = Form(media_type="application/x-www-form-urlencoded"),
    db : Session = Depends(get_db)
):
    user.add(username,email,password,db)
    url = router.url_path_for('home')
    return RedirectResponse(url,status_code=status.HTTP_303_SEE_OTHER)