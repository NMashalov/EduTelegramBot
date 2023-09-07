from sqlalchemy import Column, Integer, String,ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Homework(Base):
    __tablename__ = 'homework'

    id = Column(Integer,primary_key = True,autoincrement=True) 
    week = Column(Integer,primary_key = True,autoincrement=True)
    homework_link = Column(String)

class Homework_results(Base):
    __tablename__ = 'homework_results'

    id = Column(Integer,primary_key = True,autoincrement=True)
    homework_id = Column(Integer,ForeignKey("homework.id")) 
    user_id = Column(Integer,ForeignKey("user.id")) 
    student_homework_link = Column(Integer,primary_key = True,autoincrement=True)