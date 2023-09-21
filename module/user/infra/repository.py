from module.common.infra.repository import AlchemyRepository
from module.user.domain.entity import UserEntity
from module.user.infra.mapper import UserMapper
from module.user.infra.model import User


class UserAlchemyRepository(AlchemyRepository[UserEntity]):
    mapper = UserMapper
    model = User
