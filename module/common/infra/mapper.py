from abc import ABC, abstractmethod

from module.common.domain.entity import Entity
from module.common.infra.model import BaseModel


class IMapper(ABC):
    @staticmethod
    @abstractmethod
    def map_to_model(entity: Entity) -> BaseModel:
        ...

    @staticmethod
    @abstractmethod
    def map_to_entity(model: BaseModel) -> Entity:
        ...
