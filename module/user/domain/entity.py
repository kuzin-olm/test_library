from uuid import UUID, uuid4
from collections import defaultdict

from utils import normalize_str
from module.common.domain.entity import Entity
from module.common.domain.exception import ValidationError
from module.book.domain.entity import BookEntity
from module.rental.domain.entity import RentalBookEntity


class UserEntity(Entity):
    def __init__(self, uuid: UUID, name: str, books: list["RentalBookEntity"] = None):
        self.uuid: UUID = uuid
        self._name: str = name
        self.books: list[RentalBookEntity] = books or []

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = normalize_str(value)

    @classmethod
    def create(cls, name: str) -> "UserEntity":
        name = normalize_str(name)
        return cls(uuid=uuid4(), name=name)

    @property
    def readed_books(self) -> list[RentalBookEntity]:
        return list(filter(lambda book: book.is_read, self.books))

    @property
    def unreaded_books(self) -> list[RentalBookEntity]:
        return list(filter(lambda book: not book.is_read, self.books))

    @property
    def popularity_genre(self) -> str or None:
        rating_dict = defaultdict(int)
        for rental in self.books:
            rating_dict[rental.book.genre] += 1

        rating = sorted(rating_dict.items(), key=lambda item: item[1], reverse=True)
        try:
            popularity_genre = rating[0][0]
        except IndexError:
            popularity_genre = None
        return popularity_genre

    def add_book(self, book: BookEntity) -> None:
        if book.available_rent > 0:
            book_to_rent = RentalBookEntity.create(book=book)
            book.add_rented_book(book_to_rent)
            self.books.append(book_to_rent)
        else:
            raise ValidationError("Не осталось книг для аренды.")

    def read_book(self, rental: RentalBookEntity) -> None:
        rental.read()
