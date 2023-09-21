from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from module.common.infra.model import BaseModel


class User(BaseModel):
    __tablename__ = "user"

    name = Column(String(255), unique=True, nullable=False)

    books = relationship("RentalBook", back_populates="user")
