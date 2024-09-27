from colorama import Fore


class Assertion:
    def alert(self, error_message: str) -> None:
        print(Fore.RED+ error_message + Fore.RESET)

    def check(self, condition: bool, error_message: str) -> None:
        if not condition:
            self.alert(error_message)

