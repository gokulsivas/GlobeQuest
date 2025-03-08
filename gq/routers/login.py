from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from gq.repository.login import login_creds
from gq.database import get_db
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Login']
) 

@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return login_creds(request, db)
