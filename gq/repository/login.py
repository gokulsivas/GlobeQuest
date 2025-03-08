from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from gq.models import User_model
from gq.database import get_db
from fastapi.security import OAuth2PasswordRequestForm
from gq.hashing import Hash
from .. import JWTtoken

def login_creds(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User_model).filter(User_model.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credantials")
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password")
    
    access_token = JWTtoken.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}