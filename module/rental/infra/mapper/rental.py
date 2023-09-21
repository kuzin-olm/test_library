from module.rental.domain.entity import RentalEntity
from module.rental.infra.model import RentalBook


class RentalMapper:
    @staticmethod
    def map_to_model(entity: RentalEntity) -> RentalBook:
        return RentalBook(
            uuid=entity.uuid,
            is_read=entity.is_read,
        )

    @staticmethod
    def map_to_entity(model: RentalBook) -> RentalEntity:
        return RentalEntity(
            uuid=model.uuid,
            is_read=model.is_read,
        )
