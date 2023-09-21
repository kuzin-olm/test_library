from use_case.book.command import BookCommand
from use_case.common.handler import Handler
from use_case.common.mixin import ChoiseCommandMixin
from use_case.menu.command import MenuCommand
from use_case.renta.command import RentalCommand
from use_case.report.command import ReportCommand
from use_case.user.command import UserCommand


class HelloHandler(Handler):
    def __call__(self) -> None:
        name = input("Привет, представься пожалуйста\n")
        self.queue.append(MenuCommand())


class MenuHandler(ChoiseCommandMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_choise_cmd = {
            1: UserCommand,
            2: BookCommand,
            3: RentalCommand,
            4: ReportCommand,
        }

    def __call__(self) -> None:
        print(
            "Выберите, что хотите сделать:\n"
            "1. Создать/изменить/удалить пользователя\n"
            "2. Создать/изменить/удалить книгу\n"
            "3. Добавить факт взятия/сдачи книги\n"
            "4. Меню отчетов\n"
            "Ввести цифру"
        )
        self.handle_choise()
