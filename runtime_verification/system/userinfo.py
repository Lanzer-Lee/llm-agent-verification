from enum import Enum
from system.usersession import UserSession
from system.bankaccount import BankAccount


class UserInfo:
    class UserMode(Enum):
        ENABLED = 1
        DISABLED = 2
        FROZEN = 3

    class UserStatus(Enum):
        WHITELISTED = 1
        GREYLISTED = 2
        BLACKLISTED = 3

    class UserType(Enum):
        GOLD = 1
        SILVER = 2
        NORMAL = 3

    def __init__(self, user_id: int, name: str, country: str):
        self.next_account_number: int = 1
        self.next_session_id: int = 0
        self.sessions: list[UserSession] = []
        self.accounts: list[BankAccount] = []
        self.status: UserInfo.UserStatus | None = None
        self.type: UserInfo.UserType | None = None
        self.mode: UserInfo.UserMode | None = None
        self.user_id: int = user_id
        self.name: str = name
        self.make_disabled()
        self.make_white_listed()
        self.make_normal_user()
        self.country: str = country

    def get_id(self) -> int:
        return self.user_id

    def get_name(self) -> str:
        return self.name

    def get_country(self) -> str:
        return self.country

    def get_accounts(self) -> list[BankAccount]:
        return self.accounts

    def get_sessions(self):
        return self.sessions

    def is_gold_user(self) -> bool:
        return self.type == UserInfo.UserType.GOLD

    def is_silver_user(self) -> bool:
        return self.type == UserInfo.UserType.SILVER

    def is_normal_user(self) -> bool:
        return self.type == UserInfo.UserType.NORMAL

    def make_gold_user(self) -> None:
        # from monitor.verification import verification
        # verification.fits_making_gold_user(self)

        self.type = UserInfo.UserType.GOLD

    def make_silver_user(self) -> None:
        self.type = UserInfo.UserType.SILVER

    def make_normal_user(self) -> None:
        self.type = UserInfo.UserType.NORMAL

    def is_white_listed(self) -> bool:
        return self.status == UserInfo.UserStatus.WHITELISTED

    def is_grey_listed(self) -> bool:
        return self.status == UserInfo.UserStatus.GREYLISTED

    def is_black_listed(self) -> bool:
        return self.status == UserInfo.UserStatus.BLACKLISTED

    def make_white_listed(self) -> None:
        # from monitor.verification import verification
        # verification.user_make_white_listed(self)
        self.status = UserInfo.UserStatus.WHITELISTED

    def make_grey_listed(self) -> None:
        # from monitor.verification import verification
        # verification.user_make_grey_listed(self)
        self.status = UserInfo.UserStatus.GREYLISTED

    def make_black_listed(self) -> None:
        # from monitor.verification import verification
        # verification.user_make_black_listed(self)
        self.status = UserInfo.UserStatus.BLACKLISTED

    def is_enabled(self) -> bool:
        return self.mode == UserInfo.UserMode.ENABLED

    def is_frozen(self) -> bool:
        return self.mode == UserInfo.UserMode.FROZEN

    def is_disabled(self) -> bool:
        return self.mode == UserInfo.UserMode.DISABLED

    def make_enabled(self) -> None:
        self.mode = UserInfo.UserMode.ENABLED

    def make_frozen(self) -> None:
        self.mode = UserInfo.UserMode.FROZEN

    def make_disabled(self) -> None:
        self.mode = UserInfo.UserMode.DISABLED

    def get_session(self, session_id: int) -> UserSession | None:
        for session in self.sessions:
            if session.session_id == session_id:
                return session
        return None

    def open_session(self) -> int:
        # from monitor.verification import verification
        # verification.fits_open_session()

        session_id: int = self.next_session_id
        session = UserSession(self.user_id, session_id)
        session.open_session()
        self.sessions.append(session)
        self.next_session_id += 1

        # verification.user_open_session(self)

        return session_id

    def close_session(self, session_id: int) -> None:
        session = self.get_session(session_id)
        session.close_session()

        from monitor.verification import verification
        # verification.user_close_session(self)

    def get_account(self, account_number: str) -> BankAccount | None:
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def create_account(self, session_id: int) -> str:
        account_number = str(self.user_id) + str(self.next_account_number)
        self.next_account_number += 1
        bank_account = BankAccount(self.user_id, account_number)
        self.accounts.append(bank_account)
        return account_number

    def delete_account(self, account_number: str) -> None:
        account = self.get_account(account_number)
        account.close_account()

    def withdraw_from(self, account_number: str, amount: float) -> None:
        # from monitor.verification import verification
        # verification.user_withdrawal_solution_1(self)
        # verification.user_withdrawal_solution_2(self)
        self.get_account(account_number).withdraw(amount)

    def deposit_to(self, account_number: str, amount: float) -> None:
        self.get_account(account_number).deposit(amount)

    def get_charge_rate(self, amount: float) -> float:
        if self.is_gold_user():
            if amount <= 100:
                return 0.00
            if amount <= 1000:
                return amount * 0.02
            return amount * 0.01
        if self.is_silver_user():
            if amount <= 1000:
                return amount * 0.03
            return amount * 0.02
        if self.is_normal_user():
            if amount * 0.05 > 2.0:
                return amount * 0.05
            else:
                return 2.00
        return 0.00
