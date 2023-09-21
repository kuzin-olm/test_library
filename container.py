from module.book.infra.repository import BookAlchemyRepository
from db.database import SessionLocal
from module.user.infra.repository import UserAlchemyRepository

__all__ = ['container']


class Container:
    session = SessionLocal()

    user_repository = UserAlchemyRepository(session)
    book_repository = BookAlchemyRepository(session)


container = Container()
