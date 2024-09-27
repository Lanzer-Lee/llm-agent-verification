class UserSession:
    def __init__(self, user_id: int, session_id: int) -> None:
        self.session_id: int = session_id
        self.owner: int = user_id
        self.log: str = ""

    def get_id(self) -> int:
        return self.session_id

    def get_owner(self) -> int:
        return self.owner

    def get_log(self) -> str:
        return self.log

    def open_session(self) -> None:
        # from monitor.verification import verification
        # verification.session_open(self)
        pass

    def add_log(self, log_new: str) -> None:
        # from monitor.verification import verification
        # verification.session_log_information(self)
        self.log += log_new + "\n"

    def close_session(self) -> None:
        # from monitor.verification import verification
        # verification.session_close(self)
        pass
