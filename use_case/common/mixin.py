

class ChoiseCommandMixin:
    def handle_choise(self) -> None:
        number = self._get_choise_number()
        command = self.map_choise_cmd[number]
        self.queue.append(command())

    def _get_choise_number(self):
        while True:
            try:
                number = int(input())
                self.map_choise_cmd[number]
                return number
            except ValueError:
                print("Необходимо ввести число!")
            except KeyError:
                print("Необходимо выбрать один из вариантов.")
