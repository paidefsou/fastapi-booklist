from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, null
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    publication_year = Column(Integer, nullable=False)
    inserted_at_database = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
    
class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key = True, nullable=False)
    name = Column(String, nullable=False)
    birth_year = Column(Integer, nullable=False)
    death_year = Column(Integer, nullable = True)
    inserted_at_database = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String,nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    
class Vote(Base):
    __tablename__ = "votes"
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key = True)
    book_id = Column(Integer, ForeignKey("books.id", ondelete="CASCADE"), primary_key = True)