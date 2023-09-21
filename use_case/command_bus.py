from module.common.domain.exception import ValidationError
from use_case.menu.command import HelloCommand, MenuCommand
from use_case.menu.handler import HelloHandler, MenuHandler
from use_case.user.command import UserCommand, UserCreateCommand, UserChangeCommand, UserDeleteCommand
from use_case.book.command import BookCommand, BookCreateCommand, BookChangeCommand, BookDeleteCommand
from use_case.renta.command import RentalCommand, RentalGetCommand, RentalReturnCommand
from use_case.user.handler import UserHandler, UserCreateHandler, UserChangeHandler, UserDeleteHandler
from use_case.book.handler import BookHandler, BookCreateHandler, BookChangeHandler, BookDeleteHandler
from use_case.renta.handler import RentalHandler, RentalGetHandler, RentalReturnHandler
from use_case.report.command import (
    ReportCommand,
    QuantityBooksAndUsersCommand,
    RatingAuthorCommand,
    RatingGenreCommand,
    UsersStatisticCommand,
)
from use_case.report.handler import (
    ReportHandler,
    QuantityBooksAndUsersHandler,
    RatingAuthorBookHandler,
    RatingGenreBookHandler,
    UsersStatisticHandler,
)

_cmd_map = {
    HelloCommand: HelloHandler,
    MenuCommand: MenuHandler,
    UserCommand: UserHandler,
    UserCreateCommand: UserCreateHandler,
    UserChangeCommand: UserChangeHandler,
    UserDeleteCommand: UserDeleteHandler,
    BookCommand: BookHandler,
    BookCreateCommand: BookCreateHandler,
    BookChangeCommand: BookChangeHandler,
    BookDeleteCommand: BookDeleteHandler,
    RentalCommand: RentalHandler,
    RentalGetCommand: RentalGetHandler,
    RentalReturnCommand: RentalReturnHandler,
    ReportCommand: ReportHandler,
    QuantityBooksAndUsersCommand: QuantityBooksAndUsersHandler,
    RatingAuthorCommand: RatingAuthorBookHandler,
    RatingGenreCommand: RatingGenreBookHandler,
    UsersStatisticCommand: UsersStatisticHandler,
}


def run_input_handler():
    queue_cmd = [MenuCommand()]
    while queue_cmd:
        cmd = queue_cmd.pop(0)
        handler = _cmd_map[type(cmd)]
        try:
            handler(cmd, queue_cmd)()
        except IOError:
            ...
        except ValidationError as err:
            print(str(err))
            queue_cmd.append(MenuCommand())
