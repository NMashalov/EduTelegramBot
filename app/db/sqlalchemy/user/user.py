from sqlalchemy import Column, Integer, String,ForeignKey

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    mipt_mail = Column(String)
    telegram_id = Column(String)