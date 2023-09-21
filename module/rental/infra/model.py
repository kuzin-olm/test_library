from sqlalchemy import Column, UUID, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from module.common.infra.model import BaseModel


class RentalBook(BaseModel):
    __tablename__ = "rental_book"

    uuid_user = Column(UUID, ForeignKey("user.uuid", ondelete="CASCADE"))
    uuid_book = Column(UUID, ForeignKey("book.uuid"))
    is_read = Column(Boolean, nullable=False, default=False)

    book = relationship("Book", back_populates="rented")
    user = relationship("User", back_populates="books")
