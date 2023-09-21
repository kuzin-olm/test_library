from module.rental.infra.mapper.rental_book import RentalBookMapper
from module.user.domain.entity import UserEntity
from module.user.infra.model import User


class UserMapper:
    @staticmethod
    def map_to_model(entity: UserEntity) -> User:
        return User(
            uuid=entity.uuid,
            name=entity.name,
            books=[RentalBookMapper.map_to_model(book) for book in entity.books],
        )

    @staticmethod
    def map_to_entity(model: User) -> UserEntity:
        return UserEntity(
            uuid=model.uuid,
            name=model.name,
            books=[RentalBookMapper.map_to_entity(book) for book in model.books],
        )
