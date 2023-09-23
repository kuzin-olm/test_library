from module.common.domain.entity import Entity
from uuid import UUID, uuid4

from utils import normalize_str
from module.common.domain.exception import ValidationError
from module.rental.domain.entity import RentalEntity


class BookEntity(Entity):
    def __init__(self, uuid: UUID, title: str, author: str, genre: str, quantity: int, rented: list[RentalEntity] = None):
        self.uuid: UUID = uuid
        self._title: str = title
        self._author: str = author
        self._genre: str = genre
        self._quantity: int = quantity

        self._rented: list[RentalEntity] = rented or []

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str) -> None:
        self._title = normalize_str(value)

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, value: str) -> None:
        self._author = normalize_str(value)

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, value: str) -> None:
        self._genre = normalize_str(value)

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int) -> None:
        if value < 0:
            raise ValidationError("Количество не может быть отрицательным.")
        self._quantity = value

    @classmethod
    def create(cls, title: str, author: str, genre: str, quantity: int) -> "BookEntity":
        if quantity < 0:
            raise ValidationError("Количество не может быть отрицательным.")

        title = normalize_str(title)
        author = normalize_str(author)
        genre = normalize_str(genre)

        return cls(uuid=uuid4(), title=title, author=author, genre=genre, quantity=quantity)

    @property
    def available_rent(self) -> int:
        return self.quantity - len(list(filter(lambda rented_book: not rented_book.is_read, self._rented)))

    def add_rented_book(self, book: RentalEntity) -> None:
        self._rented.append(book)

    @property
    def quantity_rented_all_time(self) -> int:
        return len(self._rented)
