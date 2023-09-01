from fastapi import APIRouter, Depends, Request, Form, status
from db.database import get_db
from starlette.templating import Jinja2Templates
from sqlalchemy.orm import Session
from service import contact
from starlette.responses import RedirectResponse
from db.models import Message

templates = Jinja2Templates(directory="templates")

router = APIRouter(
    tags={"contact"}
)

@router.get("/contact")
def contact_page(
    request:Request,
    db:Session = Depends(get_db)
):
    return templates.TemplateResponse("contact.html",{"request":request})

@router.post("/message")
def message(
    name : str = Form(media_type="application/x-www-form-urlencode"),
    email : str = Form(media_type="application/x-www-form-urlencode"),
    phone : str = Form(media_type="application/x-www-form-urlencode"),
    message : str = Form(media_type="application/x-www-form-urlencode"),
    db : Session = Depends(get_db)
):
    new_contact = Message(
        name = name,
        email = email,
        phone = phone,
        message = message
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    url = router.url_path_for('contact_page')
    return RedirectResponse(url,status_code=status.HTTP_201_CREATED)