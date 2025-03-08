from fastapi import Depends,status,HTTPException
from gq.schemas import User_schema
from gq.models import User_model
from gq.database import get_db
from sqlalchemy.orm import Session
from gq.hashing import Hash

def create_user(request: User_schema, db: Session = Depends(get_db)):
    hashedpassword = Hash.bcrypt(request.password)
    new_user = User_model(name = request.name, email=request.email, password=hashedpassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(id: int, db: Session= Depends(get_db)):
    user = db.query(User_model).filter(User_model.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"User with id {id} is not available")
    return user