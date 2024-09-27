from monitor.assertion import Assertion


class VerificationSessionInfo:
    def __init__(self) -> None:
        self.account_request_count: int = 0
        self.session_is_open: bool = False

    def session_request_account(self) -> None:
        Assertion().check(self.account_request_count < 10, "P7 violated")
        self.account_request_count += 1

    def session_open(self) -> None:
        self.session_is_open = True

    def session_close(self) -> None:
        self.session_is_open = False

    def session_log_information(self) -> None:
        Assertion().check(self.session_is_open, "P10 violated")











