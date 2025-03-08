from fastapi import APIRouter,Depends,Response
from gq.schemas import Booking_schema, User_schema
from gq.database import get_db
from sqlalchemy.orm import Session
from typing import List
from gq.repository.booking import get_all, create, get_with_id
from gq.oauth2 import get_current_user

router = APIRouter(
    prefix="/bookings",
    tags = ['Bookings']
)

@router.get('/',response_model=List[Booking_schema])
def all(db: Session = Depends(get_db), current_user: User_schema = Depends(get_current_user)):
    return get_all(db)
    

@router.post('/')
def create_booking(request: Booking_schema, db: Session = Depends(get_db), current_user: User_schema = Depends(get_current_user)):
    return create(request, db)


@router.get('/{id}',response_model=List[Booking_schema])
def showbooking(id: int,response:Response, db: Session = Depends(get_db), current_user: User_schema = Depends(get_current_user)):
    return get_with_id(id,response,db)