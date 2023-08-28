from models import ToDo
from sqlalchemy.orm import Session
from datetime import datetime


def add_todo(
        title:str,
        db:Session,
):
    current_time = datetime.now()
    convert_to_stamp = int(round(current_time.timestamp()))
    new_todo = ToDo(
        title=title,
        created = convert_to_stamp,
        deadline = convert_to_stamp + 10800
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(todo_id:int,db:Session):
    todo = db.query(ToDo).filter(ToDo.id == todo_id).first()
    todo.status = not todo.status
    db.commit()

def delete_todo(
    id:int,
    db:Session
):
    delete = db.query(ToDo).filter(ToDo.id == id).first()
    db.delete(delete)
    db.commit()