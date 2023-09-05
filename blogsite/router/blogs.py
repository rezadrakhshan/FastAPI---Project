from fastapi import APIRouter , UploadFile, Depends
import os
from db.database import get_db
from sqlalchemy.orm import Session
from db.models import Blog
from router.home import templates
from service import blogs

router = APIRouter(
    tags=["blogs"]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Mbase = BASE_DIR.split("\\")
splited = Mbase[ 0:len(Mbase) - 1 ]
Joined = "\\".join(splited)
UPLOAD_FILE = os.path.join(Joined, "static")

@router.post("/create")
def create_blog(
    title:str,
    text:str,
    date:str,
    author:str,
    category:str,
    file:UploadFile,
    post_number:int,
    db : Session = Depends(get_db)
):
    new_filename = "{0}{1}.png".format("pic",post_number)
    SAVE_FILE_PATH = os.path.join(UPLOAD_FILE,new_filename)
    with open(SAVE_FILE_PATH,"wb") as f:
        f.write(file.file.read())
    blogs.add_blog(
        title,
        text,
        date,
        author,
        category,
        SAVE_FILE_PATH,
        db
    )

@router.delete("/delete")
def delete(
    slug:int,
    db : Session = Depends(get_db)
):
    item = db.query(Blog).filter(Blog.slug == slug).first()
    db.delete(item)
    db.commit()

