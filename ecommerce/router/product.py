from fastapi import APIRouter, File, UploadFile, Depends, Request
import os
from router.user import templates
from sqlalchemy.orm import Session
from db.datebase import get_db
from service import product
from db.models import Product
router = APIRouter(
    tags=["product"]
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
Mbase = BASE_DIR.split("/")
splited = Mbase[0:len(Mbase)-1]
joined = "\\".join(splited)

UPLOAD_FILE = os.path.join(joined, "static")


@router.post("/create")
def create_product(
    file: UploadFile,
    price:float,
    name:str,
    category:str,
    gender:str,
    post_number:int,
    detail:str,
    db:Session = Depends(get_db)
    ):
    newfile_name = "{0}{1}.png".format("pic",post_number)
    SAVE_FILE_PATH = os.path.join(UPLOAD_FILE, newfile_name)
    with open(SAVE_FILE_PATH, "wb") as f:
        f.write(file.file.read())


    return product.add_product(
        price,
        name,
        category,
        gender,
        detail,
        SAVE_FILE_PATH,
        db
    )


@router.get("/product/{product_name}")
def retrive(request:Request,product_name:str, db:Session = Depends(get_db)):
    product = db.query(Product).filter(Product.name == product_name).first()
    return templates.TemplateResponse("product.html",{"request":request,"product":product})

@router.get("/store")
def stor(request: Request, db:Session = Depends(get_db)):
    product = db.query(Product).all()
    return templates.TemplateResponse("store.html", {"request":request, "product": product})