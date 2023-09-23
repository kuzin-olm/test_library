from uuid import UUID, uuid4
from module.common.domain.entity import Entity


class RentalEntity(Entity):
    def __init__(self, uuid: UUID, is_read: bool = False):
        self.uuid = uuid
        self._is_read: bool = is_read

    @classmethod
    def create(cls) -> "RentalEntity":
        return cls(uuid=uuid4())

    @property
    def is_read(self):
        return self._is_read

    def read(self):
        self._is_read = True


class RentalBookEntity(RentalEntity):
    def __init__(self, uuid: UUID, book: "BookEntity", is_read: bool = False):
        super().__init__(uuid, is_read)
        self._book: "BookEntity" = book

    @property
    def book(self) -> "BookEntity":
        return self._book

    @classmethod
    def create(cls, book: "BookEntity") -> "RentalBookEntity":
        return cls(uuid=uuid4(), book=book)
