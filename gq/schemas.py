from pydantic import BaseModel
from typing import Optional

class Pkg_schema(BaseModel):
    title: str
    description: str
    country: str
    type: str
    nodays: int
    price: float
    imgname: str

class Show_pkg_schema(BaseModel):
    title:str
    class Config():
        orm_mode = True

class User_schema(BaseModel):
    name: str
    email: str
    password: str

class Show_user_schema(BaseModel):
    name: str
    email: str    
    class Config():
        orm_mode = True


class Booking_schema(BaseModel):
    bookedby: int
    package: int

class Login_schema(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str]= None

