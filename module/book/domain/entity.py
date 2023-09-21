from module.common.domain.entity import Entity
from uuid import UUID

from module.rental.domain.entity import RentalEntity


class BookEntity(Entity):
    def __init__(self, uuid: UUID, title: str, author: str, genre: str, quantity: int, rented: list[RentalEntity] = None):
        self.uuid: UUID = uuid
        self.title: str = title
        self.author: str = author
        self.genre: str = genre
        self.quantity: int = quantity

        self._rented: list[RentalEntity] = rented or []

    @property
    def available_rent(self) -> int:
        return self.quantity - len(list(filter(lambda rented_book: not rented_book.is_read, self._rented)))

    def add_rented_book(self, book: RentalEntity) -> None:
        self._rented.append(book)

    @property
    def quantity_rented_all_time(self) -> int:
        return len(self._rented)
