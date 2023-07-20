from fastapi import FastAPI
from router import user
from db.datebase import Base
from db import models
from db.datebase import engine
from starlette.templating import Jinja2Templates


app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.include_router(user.router)
models.Base.metadata.create_all(bind=engine)


