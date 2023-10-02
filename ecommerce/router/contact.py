from fastapi import APIRouter, File, UploadFile, Depends, Request, Form, status
import os
from router.user import templates
from sqlalchemy.orm import Session
from db.datebase import get_db
from db.models import Contact
import datetime
from starlette.responses import RedirectResponse

router = APIRouter(tags=["contact_us"])
@router.get('/contact')
def contact_creat(
    request: Request,
    db:Session = Depends(get_db),
    ):
    return templates.TemplateResponse("contact.html",{"request":request})

@router.post('/contact-create')
def contact(
    db:Session = Depends(get_db),
    name: str = Form(media_type="application/x-www-form-urlencoded"),
    email: str = Form(media_type="application/x-www-form-urlencoded"),
    subject: str = Form(media_type="application/x-www-form-urlencoded"),
    massage: str = Form(media_type="application/x-www-form-urlencoded"),
    ):

    new_contact = Contact(
        name = name,
        email = email,
        subject = subject,
        massage = massage,
        date = datetime.datetime.now()
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    url = router.url_path_for('contact_creat')
    return RedirectResponse(url,status_code=status.HTTP_303_SEE_OTHER)
