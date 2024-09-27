class BankAccount:
    def __init__(self, user_id: int, account_number: str) -> None:
        self.account_number: str = account_number
        self.balance: float = 0.00
        self.opened: bool = False
        self.owner: int = user_id

    def is_open(self) -> bool:
        return self.opened

    def get_account_number(self) -> str:
        return self.account_number

    def get_balance(self) -> float:
        return self.balance

    def get_owner(self) -> int:
        return self.owner

    def enable_account(self) -> None:
        self.opened = True

    def close_account(self) -> None:
        self.opened = False

    def withdraw(self, amount: float) -> None:
        self.balance -= amount

        # from monitor.verification import verification
        # verification.fits_account_just_accessed(self)

    def deposit(self, amount: float) -> None:
        self.balance += amount

        # from monitor.verification import verification
        # verification.fits_account_just_accessed(self)
