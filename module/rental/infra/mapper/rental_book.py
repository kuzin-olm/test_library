from module.book.infra.mapper import BookMapper
from module.rental.domain.entity import RentalBookEntity
from module.rental.infra.model import RentalBook


class RentalBookMapper:
    @staticmethod
    def map_to_model(entity: RentalBookEntity) -> RentalBook:
        return RentalBook(
            uuid=entity.uuid,
            book=BookMapper.map_to_model(entity.book),
            is_read=entity.is_read,
        )

    @staticmethod
    def map_to_entity(model: RentalBook) -> RentalBookEntity:
        return RentalBookEntity(
            uuid=model.uuid,
            book=BookMapper.map_to_entity(model.book),
            is_read=model.is_read,
        )
