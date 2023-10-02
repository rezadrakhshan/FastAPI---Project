from fastapi import FastAPI
from router import user, product, category, contact, blogs
from db.datebase import Base
from db import models
from db.datebase import engine
from starlette.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static",StaticFiles(directory="static"),name="static")
app.include_router(user.router)
app.include_router(product.router)
app.include_router(category.router)
app.include_router(contact.router)
app.include_router(blogs.router)
models.Base.metadata.create_all(bind=engine)


