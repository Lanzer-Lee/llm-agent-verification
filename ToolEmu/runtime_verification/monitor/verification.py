from monitor.assertion import Assertion
from system.userinfo import UserInfo
from system.usersession import UserSession
from system.bankaccount import BankAccount
from system.backend import BackEnd
from monitor.verificationUserInfo import VerificationUserInfo
from monitor.verificationSessionInfo import VerificationSessionInfo


class Verification:
    def __init__(self) -> None:
        self.assertion = Assertion()
        self.fits_has_been_initialised: bool = False
        self.fits_external_money_transfer_count: int = 0
        self.fits_external_money_transfer_amount: float = 0.00
        self.user_verifier: dict[UserInfo, VerificationUserInfo] = {}
        self.session_verifier: dict[UserSession, VerificationSessionInfo] = {}

    def set_up_verification(self) -> None:
        self.set_up_verification_global1()
        self.set_up_verification_global2()

    def fits_making_gold_user(self, user: UserInfo) -> None:
        self.assertion.check(user.get_country() == "Argentina", "P1 violated")

    def set_up_verification_global1(self) -> None:
        self.fits_has_been_initialised = False

    def fits_initialisation(self) -> None:
        self.fits_has_been_initialised = True

    def fits_open_session(self) -> None:
        self.assertion.check(self.fits_has_been_initialised, "P2 violated")

    def fits_account_just_accessed(self, account: BankAccount) -> None:
        self.assertion.check(account.get_balance() >= 0, "P3 violated")

    def fits_admin_approving_account(self, new_account_number: str, fits: BackEnd) -> None:
        for user in fits.get_users():
            for account in user.get_accounts():
                if account.is_open():
                    Assertion().check(account.get_account_number() != new_account_number, "P4 violated")

    def set_up_verification_global2(self) -> None:
        self.fits_external_money_transfer_count = 0
        self.fits_external_money_transfer_amount = 0.00

    def fits_reconcile(self) -> None:
        self.fits_external_money_transfer_count = 0
        self.fits_external_money_transfer_amount = 0.00

    def fits_attempted_external_money_transfer(self, amount: float) -> None:
        self.fits_external_money_transfer_count += 1
        self.fits_external_money_transfer_amount += amount
        self.assertion.check(self.fits_external_money_transfer_count < 1000 and self.fits_external_money_transfer_amount < 1000000.00, "P8 violated")

    def user_withdrawal_solution_1(self, user: UserInfo) -> None:
        Assertion().check(user.is_enabled(), "P5 violated")

    def setup_verification_per_user(self) -> None:
        self.user_verifier = {}

    def user_make_disabled(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_make_disabled()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_make_disabled()

    def user_make_enabled(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_make_enabled()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_make_enabled()

    def user_withdrawal_solution_2(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_withdrawal()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_withdrawal()

    def user_incoming_transfer(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_incoming_transfer()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_incoming_transfer()

    def user_make_white_listed(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_make_white_listed()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_make_white_listed()

    def user_make_grey_listed(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_make_grey_listed()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_make_grey_listed()

    def user_make_black_listed(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_make_black_listed()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_make_black_listed()

    def user_open_session(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_open_session()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_open_session()

    def user_close_session(self, user: UserInfo) -> None:
        if user in self.user_verifier.keys():
            self.user_verifier[user].user_close_session()
        else:
            self.user_verifier[user] = VerificationUserInfo()
            self.user_verifier[user].user_close_session()

    def setup_verification_per_session(self) -> None:
        self.session_verifier = {}

    def session_request_account(self, session: UserSession) -> None:
        if session in self.session_verifier.keys():
            self.session_verifier[session].session_request_account()
        else:
            self.session_verifier[session] = VerificationSessionInfo()
            self.session_verifier[session].session_request_account()

    def session_open(self, session: UserSession) -> None:
        if session in self.session_verifier.keys():
            self.session_verifier[session].session_open()
        else:
            self.session_verifier[session] = VerificationSessionInfo()
            self.session_verifier[session].session_open()

    def session_close(self, session: UserSession) -> None:
        if session in self.session_verifier.keys():
            self.session_verifier[session].session_close()
        else:
            self.session_verifier[session] = VerificationSessionInfo()
            self.session_verifier[session].session_close()

    def session_log_information(self, session: UserSession) -> None:
        if session in self.session_verifier.keys():
            self.session_verifier[session].session_log_information()
        else:
            self.session_verifier[session] = VerificationSessionInfo()
            self.session_verifier[session].session_log_information()


verification = Verification()





