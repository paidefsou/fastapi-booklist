from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import List, Optional
from sqlalchemy.orm import Session
from .. import models, schemas, oauth2
from ..database import get_db

from sqlalchemy import func

router = APIRouter(
    prefix="/books",
    tags=['Books']
)


@router.get("/", response_model= List[schemas.BookOut])
def books(db: Session = Depends(get_db), limit:int = 10, skip:int = 0, search:Optional[str] = ""):
    
    
   
    books = db.query(models.Book,
     func.count(models.Vote.book_id).label("votes")).join(models.Vote,
      models.Vote.book_id == models.Book.id, isouter=True).group_by(models.Book.id).filter(models.Book.title.contains(search)).limit(limit).offset(skip).all()
    return books


@router.post("/", status_code=status.HTTP_201_CREATED, response_model= schemas.Book)
def add_book(book: schemas.BookInsert, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):   
   
    new_book = models.Book(owner_id = current_user.id, **book.dict())
    db.add(new_book)        
    db.commit()
    db.refresh(new_book)
    return new_book


@router.get("/{id}", response_model= schemas.BookOut)
def get_book(id: int, db: Session = Depends(get_db), ):
  
    book = db.query(models.Book,
     func.count(models.Vote.book_id).label("votes")).join(models.Vote,
      models.Vote.book_id == models.Book.id, isouter=True).group_by(models.Book.id).first()

    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id: {id} was not found")
    return book


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):    
    
    book_query = db.query(models.Book).filter(models.Book.id == id) # this is a query

    book = book_query.first()

    if book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id:{id} does not exist")

    if book.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")


    book_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}", response_model= schemas.Book)
def update_book(id:int, updated_book: schemas.BookInsert, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)): #passing the preexisting schema for the creation of a new 
   

    book_query = db.query(models.Book).filter(models.Book.id == id) # this is a query
    book = book_query.first()
    
    if book == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Book with id:{id} does not exist")

    if book.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorised to perform requested action")
    
    book_query.update(updated_book.dict(), synchronize_session=False)
    db.commit()
    return book_query.first()