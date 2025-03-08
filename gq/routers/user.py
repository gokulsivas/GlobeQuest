from fastapi import APIRouter,Depends
from gq.schemas import User_schema, Show_user_schema
from gq.database import get_db
from sqlalchemy.orm import Session
from gq.repository.user import create_user, get_user

router = APIRouter(
    prefix="/users",
    tags = ['Users']
)

@router.post('/', response_model=Show_user_schema)
def Usercreate(request: User_schema, db: Session = Depends(get_db)):
    return create_user(request, db)

@router.get('/{id}',response_model=Show_user_schema)
def Userget(id: int, db: Session = Depends(get_db)):
    return get_user(id,db)