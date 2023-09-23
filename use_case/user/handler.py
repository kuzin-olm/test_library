from uuid import uuid4

from container import container
from module.user.domain.entity import UserEntity
from use_case.common.handler import Handler
from use_case.common.mixin import ChoiseCommandMixin
from use_case.menu.command import MenuCommand
from use_case.user.command import UserCreateCommand, UserChangeCommand, UserDeleteCommand


class UserHandler(ChoiseCommandMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_choise_cmd = {
            1: UserCreateCommand,
            2: UserChangeCommand,
            3: UserDeleteCommand,
            4: MenuCommand,
        }

    def __call__(self) -> None:
        print(
            "Выберите, что хотите сделать:\n"
            "1. Создать\n"
            "2. Изменить\n"
            "3. Удалить\n"
            "4. Вернуться в меню\n"
            "Ввести цифру"
        )
        self.handle_choise()


class UserCreateHandler(Handler):
    def __call__(self) -> None:
        print("Введите имя пользователя или 0 для выхода")
        name = input()
        if name == "0":
            self.queue.append(MenuCommand())
            return

        new_user = UserEntity.create(name=name)
        container.user_repository.save(new_user)
        print(f"Создан новый пользователь {new_user.name}")
        self.queue.append(MenuCommand())


class UserChangeHandler(Handler):
    def __call__(self) -> None:
        print("Введите имя пользователя или 0 для выхода")
        name = input()
        self.handle_exit(name, MenuCommand())

        user = container.user_repository.get_or_none(name=name)
        if user:
            print("Введите новое имя или 0 для выхода")
            new_name = input()
            self.handle_exit(new_name, MenuCommand())
            old_name = user.name
            user.name = new_name
            container.user_repository.save(user)
            print(f"Имя изменено с {old_name} -> {user.name}")
            self.queue.append(MenuCommand())
        else:
            print(f"Пользователь не найден")
            self.queue.append(UserChangeCommand())


class UserDeleteHandler(Handler):
    def __call__(self) -> None:
        name = input("Введите имя пользователя или 0 для выхода\n")
        self.handle_exit(name, MenuCommand())

        user = container.user_repository.get_or_none(name=name)
        if user:
            container.user_repository.remove(user)
            print(f"Пользователь {user.name} удален")
            self.queue.append(MenuCommand())
        else:
            print(f"Пользователь не найден")
            self.queue.append(UserDeleteCommand())
