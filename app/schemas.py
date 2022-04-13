import email
from os import access
from tkinter import E
from turtle import update
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

from pydantic.types import conint

    
# Books


class BookBase(BaseModel): 
    title: str
    publication_year: int

class BookInsert(BookBase):
    pass

class UserOut(BaseModel):  # what we send back to the user 
    id: int
    email: EmailStr # we dont sent back the password
    created_at: datetime

    class Config:
        orm_mode = True

class Book(BookBase): #the response 
    id: int
    
    inserted_at_database: datetime
    owner_id: int
    owner: UserOut   

    class Config:
        orm_mode = True
      
class BookOut(BaseModel):
    Book: Book# refers to the book above
    votes: int

    class Config:
        orm_mode = True
                
# User
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str
    
    
# Token
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None
    
class Vote(BaseModel):
    book_id: int
    dir: conint(ge=0,le=1)