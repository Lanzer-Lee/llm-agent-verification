from system.backend import BackEnd


class FrontEnd:
    def __init__(self, backend: BackEnd) -> None:
        self.backend = backend

    def get_backend(self) -> BackEnd:
        return self.backend

    def admin_initialise(self) -> None:
        self.backend.initialise()

    def admin_reconcile(self) -> None:
        # from monitor.verification import verification
        # verification.fits_reconcile()
        pass

    def admin_create_user(self, name: str, country: str) -> int:
        user_id: int = self.backend.add_user(name, country)
        self.backend.get_user_information(user_id).make_disabled()
        return user_id

    def admin_enable_user(self, user_id: int) -> None:
        # from monitor.verification import verification
        # verification.user_make_enabled(self.backend.get_user_information(user_id))
        self.backend.get_user_information(user_id).make_enabled()

    def admin_disable_user(self, user_id: int) -> None:
        # from monitor.verification import verification
        # verification.user_make_disabled(self.backend.get_user_information(user_id))
        self.backend.get_user_information(user_id).make_disabled()

    def admin_black_list_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_black_listed()

    def admin_grey_list_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_grey_listed()

    def admin_white_list_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_white_listed()

    def admin_make_gold_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_gold_user()

    def admin_make_silver_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_silver_user()

    def admin_make_normal_user(self, user_id: int) -> None:
        self.backend.get_user_information(user_id).make_normal_user()

    def admin_approve_open_account(self, user_id: int, account_number: str) -> None:
        # from monitor.verification import verification
        # verification.fits_admin_approving_account(account_number, self.backend)
        self.backend.get_user_information(user_id).get_account(account_number).enable_account()

    def admin_reject_open_account(self, user_id: int, account_number: str) -> None:
        pass

    def user_login(self, user_id: int) -> int:
        user = self.backend.get_user_information(user_id)
        if user.is_enabled():
            return user.open_session()
        else:
            return -1

    def user_logout(self, user_id: int, session_id: int) -> None:
        self.backend.get_user_information(user_id).close_session(session_id)

    def user_freeze_user(self, user_id: int, session_id: int) -> bool:
        user = self.backend.get_user_information(user_id)
        user.get_session(session_id).add_log("Freeze account")
        user.make_frozen()
        return True

    def user_unfreeze_user(self, user_id: int, session_id: int) -> bool:
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        if user.is_frozen():
            session.add_log("Unfreeze account")
            user.make_enabled()
            return True
        session.add_log("FAILED (user account not frozen): Unfreeze account")
        return False

    def user_request_account(self, user_id: int, session_id: int) -> str:
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        account_number = user.create_account(session_id)
        session.add_log("Request new account with number <" + account_number + ">")
        # from monitor.verification import verification
        # verification.session_request_account(session)
        return account_number
    
    def user_close_account(self, user_id: int, session_id: int) -> str:
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        account_number = user.create_account(session_id)
        session.add_log(f"Request new account with number <{account_number}>")
        return account_number

    def user_deposit_from_external(self, user_id: int, session_id: int, account_number_deposit: str,
                                   amount: float) -> None:
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        session.add_log(f"Deposit ${amount} to account <{account_number_deposit}>")
        user.deposit_to(account_number_deposit, amount)
        # from monitor.verification import verification
        # verification.user_incoming_transfer(user)

    def user_pay_to_external(self, user_id: int, session_id: int, account_number_source: str, amount: float) -> bool:
        # from monitor.verification import verification
        # verification.fits_attempted_external_money_transfer(amount)
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        if session is None:
            return False
        total_amount = amount + self.backend.get_user_information(user_id).get_charge_rate(amount)
        if user.get_account(account_number_source).get_balance() >= amount:
            session.add_log(f"Payment of ${amount} from account <{account_number_source}>")
            user.withdraw_from(account_number_source, total_amount)
            return True
        session.add_log(f"FAILED (not enough funds): Payment of ${amount} from account <{account_number_source}>")
        return False

    def user_transfer_to_other_account(self, user_id_source: int, session_id_source: int, account_number_source: str,
                                       user_id_deposit: int, account_number_deposit: str, amount: float) -> bool:
        from_user = self.backend.get_user_information(user_id_source)
        session = from_user.get_session(session_id_source)
        if session is None:
            return False
        total_amount = amount + self.backend.get_user_information(user_id_source).get_charge_rate(amount)
        if from_user.get_account(account_number_source).get_balance() >= total_amount:
            from_user.withdraw_from(account_number_source, total_amount)
            self.backend.get_user_information(user_id_deposit).deposit_to(account_number_deposit, amount)
            session.add_log("Payment of $" + str(
                amount) + " from account <" + account_number_source + "> to account " + "<" + account_number_deposit + " of user " + str(
                user_id_deposit))
            return True
        session.add_log("FAILED (not enough funds): " + "Payment of $" + str(
            amount) + " from account <" + account_number_source + "> to account " + "<" + account_number_deposit + " of user " + str(
            user_id_deposit))
        return False

    def user_transfer_own_accounts(self, user_id: int, session_id: int, from_account_number: str,
                                   to_account_number: str, amount: float):
        user = self.backend.get_user_information(user_id)
        session = user.get_session(session_id)
        from_account = self.backend.get_user_information(user_id).get_account(from_account_number)
        to_account = self.backend.get_user_information(user_id).get_account(to_account_number)
        if from_account.get_balance() >= amount:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            session.add_log("Transfer of $" + str(
                amount) + " from account <" + from_account_number + "> to own account <" + to_account_number)
            return True
        session.add_log("FAILED (not enough funds)" + "Transfer of $" + str(
            amount) + " from account <" + from_account_number + "> to own account <" + to_account_number)
        return False
