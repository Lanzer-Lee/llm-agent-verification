from monitor.assertion import Assertion


class VerificationUserInfo:
    def __init__(self) -> None:
        self.enabled: bool = False
        self.incoming_transfers_since_grey_listed: int = 0
        self.is_grey_listed: bool = False
        self.number_of_open_sessions: int = 0

    def user_make_disabled(self) -> None:
        self.enabled = False

    def user_make_enabled(self) -> None:
        self.enabled = True

    def is_enabled(self) -> bool:
        return self.enabled

    def user_withdrawal(self) -> None:
        Assertion().check(self.enabled, "P5 violated")

    def user_incoming_transfer(self) -> None:
        if self.is_grey_listed:
            self.incoming_transfers_since_grey_listed += 1

    def user_make_white_listed(self) -> None:
        if self.is_grey_listed:
            Assertion().check(self.incoming_transfers_since_grey_listed >= 3, "P6 violated")

    def user_make_grey_listed(self) -> None:
        if not self.is_grey_listed:
            self.incoming_transfers_since_grey_listed = 0
            self.is_grey_listed = True

    def user_make_black_listed(self) -> None:
        self.incoming_transfers_since_grey_listed = 0
        self.is_grey_listed = False

    def user_open_session(self) -> None:
        Assertion().check(self.number_of_open_sessions < 3, "P9 violated")
        self.number_of_open_sessions += 1

    def user_close_session(self) -> None:
        self.number_of_open_sessions -= 1












