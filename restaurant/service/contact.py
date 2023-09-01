from sqlalchemy.orm import Session
from db.models import Message

def add(
        name:str,email:str,phone:str,message:str,db:Session
):
    new_message = Message(
        name = phone,
        email = email,
        phone = phone,
        message = message
    )
    db.add(new_message)
    db.commit()
    db.refresh(new_message)