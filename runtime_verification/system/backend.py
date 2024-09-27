from system.userinfo import UserInfo


class BackEnd:
    def __init__(self) -> None:
        self.users: list[UserInfo] = []
        self.next_user_id: int = 1
        self.initialised: bool = False

    def get_users(self) -> list[UserInfo]:
        return self.users

    def initialise(self) -> None:
        # from monitor.verification import verification
        # verification.fits_initialisation()

        self.users = []
        self.next_user_id = 0
        self.initialised = True
        admin_user_id = self.add_user(name="Clark Kent", country="Malta")
        admin = self.get_user_information(admin_user_id)
        admin.make_silver_user()
        admin.make_enabled()

    def get_user_information(self, user_id: int) -> UserInfo | None:
        for user in self.users:
            if user.get_id() == user_id:
                return user
        return None

    def add_user(self, name: str, country: str) -> int:
        user_id = self.next_user_id
        self.next_user_id += 1
        self.users.append(UserInfo(user_id, name, country))
        return user_id
