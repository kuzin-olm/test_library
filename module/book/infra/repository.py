from module.common.infra.repository import AlchemyRepository
from module.book.domain.entity import BookEntity
from module.book.infra.mapper import BookMapper
from module.book.infra.model import Book


class BookAlchemyRepository(AlchemyRepository[BookEntity]):
    mapper = BookMapper
    model = Book
