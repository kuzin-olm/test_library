from uuid import UUID
from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from sqlalchemy.orm import Session

from module.common.domain.entity import Entity
from module.common.domain.exception import LibraryError
from .mapper import IMapper
from .model import BaseModel


E = TypeVar("E", bound=Entity)


class Repository(Generic[E], ABC):

    @abstractmethod
    def save(self, entity: E) -> None:
        ...

    def remove(self, entity: E) -> None:
        ...

    @abstractmethod
    def get_by_uuid(self, uuid: UUID) -> E:
        ...

    def __getitem__(self, uuid) -> E:
        return self.get_by_uuid(uuid)


class AlchemyRepository(Repository[E], ABC):
    mapper: IMapper = None
    model: BaseModel = None

    def __init__(self, session: Session):
        self._session = session

    def save(self, entity: E) -> None:
        self._session.merge(self.mapper.map_to_model(entity))
        self._session.commit()

    def get_or_none(self, **kwargs) -> E or None:
        model = self._session.query(self.model).filter_by(**kwargs).one_or_none()
        return model and self.mapper.map_to_entity(model)

    def get_by_uuid(self, uuid: str) -> E:
        model = self._session.query(self.model).get(uuid)
        return self.mapper.map_to_entity(model)

    def get_by_optional(self, **kwargs) -> list[E]:
        return [self.mapper.map_to_entity(model) for model in self._session.query(self.model).filter_by(**kwargs).all()]

    def get_all(self) -> list[E]:
        return [self.mapper.map_to_entity(model) for model in self._session.query(self.model).all()]

    def remove(self, entity: E) -> None:
        self._session.query(self.model).filter_by(uuid=entity.uuid).delete()
        self._session.commit()


class InMemoryRepository(Repository[E]):
    def __init__(self, items: dict[UUID, E] = None):
        self._items = items or dict()

    def get_by_uuid(self, uuid) -> E:
        try:
            return self._items[uuid]
        except KeyError:
            raise LibraryError(f"{uuid} does not exist")

    def remove(self, entity: E) -> None:
        try:
            self._items.pop(entity.uuid)
        except KeyError:
            raise LibraryError(f"{entity.uuid} does not exist")

    def save(self, entity: E) -> None:
        self._items[entity.uuid] = entity
