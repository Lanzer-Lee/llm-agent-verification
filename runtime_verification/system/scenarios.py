from system.frontend import FrontEnd
from system.transactionsystem import TransactionSystem
from colorama import Fore


class Scenarios:
    def __init__(self):
        self.SCENARIO_COUNT = 20
        self.transaction_system: TransactionSystem = TransactionSystem()

    def run_scenario(self, n: int) -> None:
        frontend: FrontEnd = self.transaction_system.get_frontend()
        if 0 < n <= self.SCENARIO_COUNT:
            prop = (n + 1) // 2
            print(Fore.BLUE + f"\nRunning scenario {n}." + Fore.RESET)
            print("This scenario should " + ("" if n % 2 == 1 else "not ") + "violate property " + str(prop) + ".")
        match n:
            case 1:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                frontend.admin_make_gold_user(user_id)
            case 2:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                frontend.admin_make_silver_user(user_id)
                user_id = frontend.admin_create_user(name="Marge", country="Argentina")
                frontend.admin_enable_user(user_id)
                frontend.admin_make_gold_user(user_id)
            case 3:
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                frontend.user_login(user_id)
            case 4:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                frontend.user_logout(user_id, session_id)
            case 5:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_deposit_from_external(user_id, session_id, account_number, amount=500.00)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=495.00)
            case 6:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_deposit_from_external(user_id, session_id, account_number, amount=500.00)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=100.00)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=100.00)
            case 7:
                frontend.admin_initialise()
                for i in range(15):
                    user_id = frontend.admin_create_user(f"Fred({i})", country="France")
                    frontend.admin_enable_user(user_id)
                    for j in range(11):
                        session_id = frontend.user_login(user_id)
                        account_number = frontend.user_request_account(user_id, session_id)
                        frontend.admin_approve_open_account(user_id, account_number)
                        frontend.user_logout(user_id, session_id)
            case 8:
                frontend.admin_initialise()
                for i in range(10):
                    user_id = frontend.admin_create_user(f"Fred({i})", country="France")
                    frontend.admin_enable_user(user_id)
                    session_id = frontend.user_login(user_id)
                    for j in range(10):
                        account_number = frontend.user_request_account(user_id, session_id)
                        frontend.admin_approve_open_account(user_id, account_number)
                    frontend.user_logout(user_id, session_id)
            case 9:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_deposit_from_external(user_id, session_id, account_number, amount=500.00)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=1000.00)
                frontend.admin_disable_user(user_id)
                frontend.user_freeze_user(user_id, session_id)
                frontend.user_unfreeze_user(user_id, session_id)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=200.00)
            case 10:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_deposit_from_external(user_id, session_id, account_number, amount=500.00)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=1000.00)
                frontend.admin_disable_user(user_id)
                frontend.admin_enable_user(user_id)
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=200.00)
            case 11:
                frontend.admin_initialise()
                user_id_receiver = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id_receiver)
                session_id_receiver = frontend.user_login(user_id_receiver)
                account_number_receiver = frontend.user_request_account(user_id_receiver, session_id_receiver)
                frontend.admin_approve_open_account(user_id_receiver, account_number_receiver)
                frontend.user_logout(user_id_receiver, session_id_receiver)
                user_id = frontend.admin_create_user(name="Sandy", country="Senegal")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_logout(user_id, session_id)
                frontend.admin_grey_list_user(user_id)
                for i in range(2):
                    session_id = frontend.user_login(user_id)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                    frontend.user_logout(user_id, session_id)
                frontend.admin_white_list_user(user_id)
            case 12:
                frontend.admin_initialise()
                user_id_receiver = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id_receiver)
                session_id_receiver = frontend.user_login(user_id_receiver)
                account_number_receiver = frontend.user_request_account(user_id_receiver, session_id_receiver)
                frontend.admin_approve_open_account(user_id_receiver, account_number_receiver)
                frontend.user_logout(user_id_receiver, session_id_receiver)
                user_id = frontend.admin_create_user(name="Sandy", country="Senegal")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_logout(user_id, session_id)
                frontend.admin_grey_list_user(user_id)
                for i in range(2):
                    session_id = frontend.user_login(user_id)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=100.00)
                    frontend.user_logout(user_id, session_id)
                frontend.admin_white_list_user(user_id)
            case 13:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                for i in range(11):
                    account_number = frontend.user_request_account(user_id, session_id)
                    if i % 2 == 0:
                        frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_logout(user_id, session_id)
            case 14:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Fred", country="France")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                for i in range(30):
                    account_number = frontend.user_request_account(user_id, session_id)
                    if i % 2 == 0:
                        frontend.admin_approve_open_account(user_id, account_number)
                    if i % 9 == 5:
                        frontend.user_logout(user_id, session_id)
                        session_id = frontend.user_login(user_id)
                frontend.user_logout(user_id, session_id)
            case 15:
                frontend.admin_initialise()
                for i in range(50):
                    user_id = frontend.admin_create_user(f"Fred({i})", "France")
                    frontend.admin_enable_user(user_id)
                    session_id = frontend.user_login(user_id)
                    account_number = frontend.user_request_account(user_id, session_id)
                    frontend.admin_approve_open_account(user_id, account_number)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=25000.00)
                    frontend.user_pay_to_external(user_id, session_id, account_number, amount=20000.00)
                    frontend.user_logout(user_id, session_id)
            case 16:
                total: int = 0
                frontend.admin_initialise()
                for i in range(1000):
                    user_id = frontend.admin_create_user(f"Fred({i})", country="France")
                    frontend.admin_enable_user(user_id)
                    session_id = frontend.user_login(user_id)
                    account_number = frontend.user_request_account(user_id, session_id)
                    frontend.admin_approve_open_account(user_id, account_number)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                    frontend.user_pay_to_external(user_id, session_id, account_number, amount=500.00)
                    total += 1525
                    if total > 500000:
                        frontend.admin_reconcile()
                    frontend.user_logout(user_id, session_id)
            case 17:
                frontend.admin_initialise()
                for i in range(4):
                    user_id = frontend.admin_create_user(f"Fred({i})", "France")
                    frontend.admin_enable_user(user_id)
                    for j in range(i + 1):
                        session_id = frontend.user_login(user_id)
            case 18:
                frontend.admin_initialise()
                for i in range(4):
                    user_id = frontend.admin_create_user(f"Fred({i})", "France")
                    frontend.admin_enable_user(user_id)
                    for j in range(5):
                        session_id = frontend.user_login(user_id)
                        frontend.user_logout(user_id, session_id)
                    for j in range(2):
                        session_id = frontend.user_login(user_id)
            case 19:
                frontend.admin_initialise()
                user_id_receiver = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id_receiver)
                session_id_receiver = frontend.user_login(user_id_receiver)
                account_number_receiver = frontend.user_request_account(user_id_receiver, session_id_receiver)
                frontend.admin_approve_open_account(user_id_receiver, account_number_receiver)
                frontend.user_logout(user_id_receiver, session_id_receiver)
                for i in range(5):
                    user_id = frontend.admin_create_user(f"Sandy({i})", country="Senegal")
                    frontend.admin_enable_user(user_id)
                    session_id = frontend.user_login(user_id)
                    account_number = frontend.user_request_account(user_id, session_id)
                    frontend.admin_approve_open_account(user_id, account_number)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                    frontend.user_logout(user_id, session_id)
                    if i == 3:
                        frontend.user_pay_to_external(user_id, session_id, account_number, amount=100.00)
            case 20:
                frontend.admin_initialise()
                user_id_receiver = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id_receiver)
                session_id_receiver = frontend.user_login(user_id_receiver)
                account_number_receiver = frontend.user_request_account(user_id_receiver, session_id_receiver)
                frontend.admin_approve_open_account(user_id_receiver, account_number_receiver)
                frontend.user_logout(user_id_receiver, session_id_receiver)
                for i in range(5):
                    user_id = frontend.admin_create_user(f"Sandy({i})", country="Senegal")
                    frontend.admin_enable_user(user_id)
                    session_id = frontend.user_login(user_id)
                    account_number = frontend.user_request_account(user_id, session_id)
                    frontend.admin_approve_open_account(user_id, account_number)
                    frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                    frontend.user_pay_to_external(user_id, session_id, account_number, amount=100.00)
                    frontend.user_transfer_to_other_account(user_id, session_id, account_number, user_id_receiver,
                                                            account_number_receiver, amount=100.00)
                    frontend.user_logout(user_id, session_id)
            case 21:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                print("Time is fast-forwarded by 00h00m03s")
                frontend.user_login(user_id)
            case 22:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                print("Time is fast-forwarded by 00h00m21s")
                frontend.user_login(user_id)
            case 23:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                frontend.user_deposit_from_external(user_id, session_id, account_number, amount=1000.00)
                frontend.admin_black_list_user(user_id)
                print("Time is fast-forwarded by 00h00m03s")
                frontend.admin_white_list_user(user_id)
                print("Time is fast-forwarded by 10h30m00s")
                frontend.user_pay_to_external(user_id, session_id, account_number, amount=120.00)
            case 24:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                account_number1 = frontend.user_request_account(user_id, session_id)
                account_number2 = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number1)
                frontend.admin_approve_open_account(user_id, account_number2)
                frontend.user_deposit_from_external(user_id, session_id, account_number1, amount=1000.00)
                frontend.admin_black_list_user(user_id)
                print("Time is fast-forwarded by 00h00m03s")
                frontend.admin_white_list_user(user_id)
                print("Time is fast-forwarded by 10h30m00s")
                frontend.user_pay_to_external(user_id, session_id, account_number1, amount=80.00)
                frontend.user_pay_to_external(user_id, session_id, account_number2, amount=70.00)
                frontend.user_transfer_own_accounts(user_id, session_id, account_number1, account_number2,
                                                    amount=120.00)
                print("Time is fast-forwarded by 05h20m00s")
                frontend.user_pay_to_external(user_id, session_id, account_number1, amount=140.00)
            case 25:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                print("Time is fast-forwarded by 23h00m00s")
                account_number = frontend.user_request_account(user_id, session_id)
                frontend.admin_approve_open_account(user_id, account_number)
                print("Time is fast-forwarded by 03h00m00s")
                account_number1 = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 12h10m00s")
                account_number2 = frontend.user_request_account(user_id, session_id)
            case 26:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                print("Time is fast-forwarded by 23h00m00s")
                account_number = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 03h00m00s")
                account_number1 = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 21h10m00s")
                account_number2 = frontend.user_request_account(user_id, session_id)
            case 27:
                frontend.admin_initialise()
                print("Time is fast-forwarded by 00h07m00s")
            case 28:
                frontend.admin_initialise()
                print("Time is fast-forwarded by 00h03m00s")
                frontend.admin_reconcile()
            case 29:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                print("Time is fast-forwarded by 00h03m00s")
                account_number = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 00h01m00s")
                frontend.user_logout(user_id, session_id)
                print("Time is fast-forwarded by 99h00m00s")
            case 30:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                print("Time is fast-forwarded by 00h03m00s")
                account_number1 = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 00h03m00s")
                account_number2 = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 00h02m00s")
                frontend.admin_approve_open_account(user_id, account_number1)
                print("Time is fast-forwarded by 00h04m00s")
                frontend.user_logout(user_id, session_id)
                print("Time is fast-forwarded by 22h04m00s")
                frontend.admin_reject_open_account(user_id, account_number2)
            case 31:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id = frontend.user_login(user_id)
                print("Time is fast-forwarded by 00h03m00s")
                account_number = frontend.user_request_account(user_id, session_id)
                print("Time is fast-forwarded by 00h10m00s")
                frontend.admin_approve_open_account(user_id, account_number)
                print("Time is fast-forwarded by 00h08m00s")
            case 32:
                frontend.admin_initialise()
                user_id = frontend.admin_create_user(name="Roger", country="Romania")
                frontend.admin_enable_user(user_id)
                session_id1 = frontend.user_login(user_id)
                print("Time is fast-forwarded by 00h3m00s")
                session_id2 = frontend.user_login(user_id)
                print("Time is fast-forwarded by 00h03m00s")
                account_number = frontend.user_request_account(user_id, session_id1)
                print("Time is fast-forwarded by 00h10m00s")
                frontend.admin_approve_open_account(user_id, account_number)
                print("Time is fast-forwarded by 00h01m00s")
                frontend.user_logout(user_id, session_id2)
                print("Time is fast-forwarded by 00h02m00s")
                frontend.user_logout(user_id, session_id1)
            case _:
                print(f"Requested scenario {n} which is not defined.")

    def run_violating_scenario_for_property(self, n: int) -> None:
        self.run_scenario(2 * n - 1)

    def run_non_violating_scenario_for_property(self, n: int) -> None:
        self.run_scenario(2 * n)

    def run_non_scenarios_for_property(self, n: int) -> None:
        self.run_violating_scenario_for_property(n)
        self.run_non_violating_scenario_for_property(n)

    def reset_scenarios(self) -> None:
        from monitor.verification import verification
        verification.set_up_verification()

        self.transaction_system.setup()

    def run_all_scenarios(self) -> None:
        for n in range(1, self.SCENARIO_COUNT + 1):
            self.reset_scenarios()

            self.run_scenario(n)

