from app.models.base import Base
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column 

from sqlalchemy.orm import relationship

class Question(Base):
    __tablename__ = 'question'

    id: Mapped[int] = mapped_column(primary_key =True)
    question_text: Mapped[str]
    week: Mapped[str]
    answers: Mapped['Answer'] = relationship(backref="question",lazy = 'selectin') 
    

class Answer(Base):
    __tablename__ = 'answer'
    id: Mapped[int] = mapped_column(primary_key =True)
    question_id = mapped_column(ForeignKey("question.id")) 
    answer_text: Mapped[str]
    is_right: Mapped[int]

class UserQuizResults(Base):
    __tablename__ = 'user_quiz_results'
    id: Mapped[int] = mapped_column(primary_key =True)
    quiz_week: Mapped[int] = mapped_column(server_default=0)
    quiz_results: Mapped[int] = mapped_column(server_default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    

    
    