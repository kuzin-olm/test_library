from uuid import UUID
from module.common.domain.entity import Entity


class RentalEntity(Entity):
    def __init__(self, uuid: UUID, is_read: bool = False):
        self.uuid = uuid
        self.is_read: bool = is_read

    def read(self):
        self.is_read = True


class RentalBookEntity(RentalEntity):
    def __init__(self, uuid: UUID, book: "BookEntity", is_read: bool = False):
        super().__init__(uuid, is_read)
        self.book: "BookEntity" = book
