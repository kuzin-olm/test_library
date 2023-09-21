from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from module.common.infra.model import BaseModel


class Book(BaseModel):
    __tablename__ = "book"

    title: str = Column(String(255), unique=True)
    author: str = Column(String(255), nullable=False)
    genre: str = Column(String(100), nullable=False)
    quantity: int = Column(Integer, nullable=False)

    rented = relationship("RentalBook", back_populates="book")
    