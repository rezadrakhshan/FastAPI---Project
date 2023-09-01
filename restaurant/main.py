from fastapi import FastAPI, Request, Depends
from fastapi.templating import Jinja2Templates
from db.database import get_db
from db import models
from db.database import engine
from router import food, contact
from sqlalchemy.orm import Session
from db.models import Menu

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
templates = Jinja2Templates(directory="templates")
app.include_router(food.router)
app.include_router(contact.router)


@app.get("/")
def home(
    request:Request
):
    return templates.TemplateResponse("index.html",{"request":request})

@app.get("/about")
def about(
    request:Request
):
    return templates.TemplateResponse("about.html",{"request":request})
@app.get("/menu")
def menu(
    request:Request,
    db:Session = Depends(get_db)
):
    menu = db.query(Menu).all()
    return templates.TemplateResponse("menu.html",{"request":request,"menu":menu})

@app.get("/contact")
def contact(
    request:Request
):
    return templates.TemplateResponse("contact.html",{"request":request})