from app.models.base import Base
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column 

class User(Base):
    __tablename__ = "user"

    id: Mapped[int]= mapped_column(primary_key=True)
    name: Mapped[str] 
    mipt_mail: Mapped[str] = mapped_column(default='') 
    admin: Mapped[bool] = mapped_column(server_default=False)
