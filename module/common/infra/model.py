import uuid as uuid
from sqlalchemy import Column, UUID

from db.database import Base


class BaseModel(Base):
    __abstract__ = True

    uuid = Column(UUID, primary_key=True, default=uuid.uuid4, nullable=False)
