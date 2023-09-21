from uuid import uuid4

from container import container
from module.book.domain.entity import BookEntity
from use_case.common.handler import Handler
from use_case.common.mixin import ChoiseCommandMixin
from use_case.menu.command import MenuCommand
from use_case.book.command import BookCreateCommand, BookChangeCommand, BookDeleteCommand


class BookHandler(ChoiseCommandMixin, Handler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.map_choise_cmd = {
            1: BookCreateCommand,
            2: BookChangeCommand,
            3: BookDeleteCommand,
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


class BookCreateHandler(Handler):
    def __call__(self) -> None:
        title = self.handle_input("Введите название\n")
        author = self.handle_input("Введите автора\n")
        genre = self.handle_input("Введите жанр\n")
        quantity = self.handle_input("Введите доступное кол-во\n", to_type=int)
        new_book = BookEntity(uuid=uuid4(), title=title, author=author, genre=genre, quantity=quantity)
        container.book_repository.save(new_book)
        print(f"Книга {new_book.title} создана, доступно {new_book.available_rent}")
        self.queue.append(MenuCommand())


class BookChangeHandler(Handler):
    def __call__(self) -> None:
        title = input("Введите название\n")
        book = container.book_repository.get_or_none(title=title)
        if book:
            book.title = self.handle_input(f"Введите новое название (текущее: {book.title})\n")
            book.author = self.handle_input(f"Введите нового автора  (текущий: {book.author})\n")
            book.genre = self.handle_input(f"Введите новый жанр (текущий: {book.genre})\n")
            book.quantity = self.handle_input(f"Введите доступное кол-во  (текущее: {book.quantity})\n", to_type=int)
            container.book_repository.save(book)
            print(f"Книга {book.title} изменена")
            self.queue.append(MenuCommand())
        else:
            print(f"Книга не найдена")
            self.queue.append(BookChangeCommand())


class BookDeleteHandler(Handler):
    def __call__(self) -> None:
        title = self.handle_input("Введите название\n")
        book = container.book_repository.get_or_none(title=title)
        if book:
            container.book_repository.remove(book)
            print(f"Книга {book.title} удалена")
            self.queue.append(MenuCommand())
        else:
            print(f"Книга не найдена")
            self.queue.append(BookDeleteCommand())
