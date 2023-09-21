from container import container
from use_case.common.handler import Handler
from use_case.common.mixin import ChoiseCommandMixin
from use_case.menu.command import MenuCommand
from use_case.renta.command import RentalGetCommand, RentalReturnCommand


class RentalHandler(ChoiseCommandMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_choise_cmd = {
            1: RentalGetCommand,
            2: RentalReturnCommand,
            3: MenuCommand,
        }

    def __call__(self) -> None:
        print(
            "Выберите, что хотите сделать:\n"
            "1. Взять книгу\n"
            "2. Сдать книгу\n"
            "3. Вернуться в меню\n"
            "Ввести цифру"
        )
        self.handle_choise()


class RentalGetHandler(Handler):
    def __call__(self) -> None:
        book = self.fetch_book()
        user = self.fetch_user()
        user.add_book(book)
        container.user_repository.save(user)
        print(f"Книга {book.title} успешно записана на {user.name}")
        self.queue.append(MenuCommand())

    def fetch_book(self):
        while True:
            title = self.handle_input("Название книги\n")
            book = container.book_repository.get_or_none(title=title)
            if not book:
                print(f"Книга не найдена")
                continue
            if book.available_rent == 0:
                print(f"Не осталось книг {book.title} для аренды")
                continue
            return book

    def fetch_user(self):
        while True:
            user_name = self.handle_input("На кого записываем\n")
            user = container.user_repository.get_or_none(name=user_name)
            if not user:
                print(f"Пользователь не найден")
                continue
            return user


class RentalReturnHandler(Handler):
    def __call__(self) -> None:
        user = self.fetch_user()

        if not user.unreaded_books:
            print(f"У пользователя {user.name} нет не сданных книг")
            self.queue.append(MenuCommand())
            return

        books_map = {idx: rental for idx, rental in enumerate(user.unreaded_books, start=1)}
        print("Не сданные книги польователя:")
        for idx, rental in books_map.items():
            print(f"{idx}. {rental.book.title}")

        rental_book = self.handle_input_choise_book(books_map)
        user.read_book(rental_book)
        container.user_repository.save(user)

        print(f"Пользователь {user.name} сдал книгу {rental_book.book.title}")
        self.queue.append(MenuCommand())

    def fetch_user(self):
        while True:
            user_name = self.handle_input("Имя пользователя, который хочет сдать книгу\n")
            user = container.user_repository.get_or_none(name=user_name)
            if not user:
                print(f"Пользователь не найден")
                continue
            return user

    def handle_input_choise_book(self, book_map: dict):
        while True:
            number = self.handle_input("Выберите книгу, которую хотите сдать\n", to_type=int)
            try:
                return book_map[number]
            except KeyError:
                print("Такого варианта нет")
