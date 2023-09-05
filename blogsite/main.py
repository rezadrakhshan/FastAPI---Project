from fastapi import FastAPI
from db.database import engine
from db import models
from router import home,category,blogs
from fastapi.staticfiles import StaticFiles

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(home.router)
app.include_router(category.router)
app.include_router(blogs.router)

