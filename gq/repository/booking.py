from fastapi import Depends,status, HTTPException, Response 
from gq.schemas import Booking_schema
from gq.models import Booking_model
from gq.database import get_db
from sqlalchemy.orm import Session

def get_all(db):
    bookings = db.query(Booking_model).all()
    return bookings

def create(request: Booking_schema, db: Session = Depends(get_db)):
    new_booking = Booking_model(bookedby = request.bookedby,
                                package= request.package)
    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    return new_booking

def get_with_id(id, response: Response, db: Session = Depends(get_db)):
    books = db.query(Booking_model).filter(Booking_model.id == id).all()
    if not books:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,details=f"Booking with id {id} is not available")
    return books