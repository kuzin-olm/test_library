from .command import Command
from ..menu.command import MenuCommand


class Handler:
    def __init__(self, command: Command, queue: list[Command]):
        self.command = command
        self.queue = queue

    def __call__(self) -> None:
        ...

    def handle_exit(self, input_: str, next_: Command) -> None:
        if input_ == "0":
            self.queue.append(next_)
            raise IOError

    def handle_input(self, msg: str, to_type: type = None):
        while True:
            value = input(msg)
            self.handle_exit(value, MenuCommand())
            if to_type:
                try:
                    return to_type(value)
                except ValueError:
                    print("Неккоректный ввод")
            else:
                return value
