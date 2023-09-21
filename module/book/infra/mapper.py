
from module.book.domain.entity import BookEntity
from module.book.infra.model import Book
from module.rental.infra.mapper.rental import RentalMapper


class BookMapper:
    @staticmethod
    def map_to_model(entity: BookEntity) -> Book:
        return Book(
            uuid=entity.uuid,
            title=entity.title,
            author=entity.author,
            genre=entity.genre,
            quantity=entity.quantity,
        )

    @staticmethod
    def map_to_entity(model: Book) -> BookEntity:
        return BookEntity(
            uuid=model.uuid,
            title=model.title,
            author=model.author,
            genre=model.genre,
            quantity=model.quantity,
            rented=[RentalMapper.map_to_entity(model) for model in model.rented]
        )
