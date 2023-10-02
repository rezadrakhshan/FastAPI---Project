from sqlalchemy.orm import Session
from db.models import User

def add(
    username:str,email:str,password:int,db:Session
):
    new_user = User(
        name=username,
        password=password,
        email=email,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

    