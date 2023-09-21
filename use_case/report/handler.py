from collections import defaultdict

from container import container
from use_case.common.handler import Handler
from use_case.common.mixin import ChoiseCommandMixin
from use_case.menu.command import MenuCommand
from use_case.report.command import (
    QuantityBooksAndUsersCommand,
    RatingAuthorCommand,
    RatingGenreCommand,
    UsersStatisticCommand, ReportCommand,
)


class ReportHandler(ChoiseCommandMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_choise_cmd = {
            1: QuantityBooksAndUsersCommand,
            2: RatingAuthorCommand,
            3: RatingGenreCommand,
            4: UsersStatisticCommand,
            5: MenuCommand,
        }

    def __call__(self) -> None:
        print(
            "Выберите, что хотите сделать:\n"
            "1. Количество зарегестрированных книг и пользователей\n"
            "2. Самый читаемый автор\n"
            "3. Самые предпочитаемые читателями жанры по убыванию\n"
            "4. Статистика по пользователям\n"
            "5. Вернуться в меню\n"
            "Ввести цифру"
        )
        self.handle_choise()


class QuantityBooksAndUsersHandler(Handler):
    def __call__(self) -> None:
        users = container.user_repository.get_all()
        books = container.book_repository.get_all()
        print(
            "В библиотеке зарегестрированно:\n"
            f"\tпользователей - {len(users)}\n"
            f"\tкниг - {len(books)}"
        )
        self.queue.append(ReportCommand())


class RatingBookHandler(Handler):
    key_rating = None

    def __call__(self) -> None:
        assert self.key_rating is not None, "необходимо указать ключ ранжирования"
        books = container.book_repository.get_all()
        rating_dict = defaultdict(int)
        print("Рейтинг в порядке убывания:")
        for book in books:
            rating_dict[getattr(book, self.key_rating)] += book.quantity_rented_all_time
        for key, qty in sorted(rating_dict.items(), key=lambda item: item[1], reverse=True):
            print(f"\t{key}")
        self.queue.append(ReportCommand())


class RatingAuthorBookHandler(RatingBookHandler):
    key_rating = "author"


class RatingGenreBookHandler(RatingBookHandler):
    key_rating = "genre"


class UsersStatisticHandler(Handler):
    def __call__(self) -> None:
        users = container.user_repository.get_all()
        print("Статистика по пользователям:")
        for user in users:
            qty_books = len(user.books)
            qty_unreaded_books = len(user.unreaded_books)
            popularity_genre = user.popularity_genre or "отсутствует"

            print(
                f"\t{user.name}: "
                f"всего книг - {qty_books}, "
                f"из них не сданны - {qty_unreaded_books}, "
                f"любимый жанр - {popularity_genre}"
            )

        self.queue.append(ReportCommand())
