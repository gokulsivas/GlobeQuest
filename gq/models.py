from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from gq.database import Base

class Pkg_model(Base):
    __tablename__ = 'tourpackage'
    id= Column(Integer,primary_key=True,index=True)
    title=Column(String(25), unique=True)
    description=Column(String(500))
    country=Column(String(255))
    type=Column(String(100))
    nodays=Column(Integer)
    price=Column(Float)
    imgname=Column(String(100))

class User_model(Base):
    __tablename__ = 'users'
    id= Column(Integer,primary_key=True,index=True)
    name=Column(String(25))
    email=Column(String(100))
    password=Column(String(1000))

class Booking_model(Base):
    __tablename__ = 'bookings'
    id= Column(Integer, primary_key=True, index=True)
    bookedby= Column(Integer, ForeignKey('users.id'))
    package=Column(Integer, ForeignKey('tourpackage.id'))
    
class Login_model(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    password = Column(String)