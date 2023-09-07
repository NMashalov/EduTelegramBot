from sqlalchemy import Column, Integer, String,ForeignKey

from sqlalchemy.orm import declarative_base,relationship

Base = declarative_base()

class Questions(Base):
    __tablename__ = 'questions'

    question_id = Column(Integer,primary_key =True, autoincrement=True)
    question_text = Column(String)
    week = Column(Integer) 

class Answers(Base):
    __tablename__ = 'answers'

    answer_id = Column(Integer,primary_key =True, autoincrement=True)
    question_id = Column(String,ForeignKey('questions.question_id'))
    week = Column(Integer) 

    user = relationship("Questions", backref="answers")