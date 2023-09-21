from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column 
from app.models.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime
from app.models import User
from typing import List

class Homework(Base):
    __tablename__ = 'homework'
    id: Mapped[int] = mapped_column(primary_key = True) 
    week: Mapped[int]
    description: Mapped[str]
    homework_link: Mapped[str]

class UserHomeworkResults(Base):
    __tablename__ = 'homework_results'
 
    id: Mapped[int] = mapped_column(primary_key = True) 
    homework_id : Mapped[int] = mapped_column(ForeignKey("homework.id")) 
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id")) 
    student_homework_link: Mapped[str]
    result: Mapped[int]
    valid_from_dttm: Mapped[DateTime]
    # 
    user: Mapped["User"] = relationship(back_populates="user_homework_results")
    homework: Mapped["Homework"] = relationship()
