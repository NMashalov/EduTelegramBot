from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 
from app.models.base import Base


class Homework(Base):
    __tablename__ = 'homework'
    id: Mapped[int] = mapped_column(primary_key = True) 
    week:Mapped[int]
    homework_link: Mapped[str]

class Homework_results(Base):
    __tablename__ = 'homework_results'

    id: Mapped[int] = mapped_column(primary_key = True) 
    homework_id : Mapped[int] = mapped_column(ForeignKey("homework.id")) 
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id")) 
    student_homework_link: Mapped[str]

class Homework_assign(Base):
    __tablename__ = 'homework_questions'

    id: Mapped[int] = mapped_column(primary_key = True)
    homework_id : Mapped[int] = mapped_column(ForeignKey("homework.id"))
    question: Mapped[str]
    question_type: Mapped[str]