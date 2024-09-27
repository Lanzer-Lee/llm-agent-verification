import json
from system.frontend import FrontEnd
from system.transactionsystem import TransactionSystem
from monitor import properties
from monitor.verification import verification
from colorama import Fore


function_map = {
    "FitsAdministratorApproveOpenAccount": FrontEnd.admin_approve_open_account,
    "FitsAdministratorBlackListUser": FrontEnd.admin_black_list_user,
    "FitsAdministratorCreateUser": FrontEnd.admin_create_user,
    "FitsAdministratorDisableUser": FrontEnd.admin_disable_user,
    "FitsAdministratorEnableUser": FrontEnd.admin_enable_user,
    "FitsAdministratorGreyListUser": FrontEnd.admin_grey_list_user,
    "FitsAdministratorInitialise": FrontEnd.admin_initialise,
    "FitsAdministratorMakeGoldUser": FrontEnd.admin_make_gold_user,
    "FitsAdministratorMakeNormalUser": FrontEnd.admin_make_normal_user,
    "FitsAdministratorMakeSilverUser": FrontEnd.admin_make_silver_user,
    "FitsAdministratorReconcile": FrontEnd.admin_reconcile,
    "FitsAdministratorRejectOpenAccount": FrontEnd.admin_reject_open_account,
    "FitsAdministratorWhiteListUser": FrontEnd.admin_white_list_user,
    "FitsUserCloseAccount": FrontEnd.user_close_account,
    "FitsUserFreezeUser": FrontEnd.user_freeze_user,
    "FitsUserDepositFromExternal": FrontEnd.user_deposit_from_external,
    "FitsUserPayToExternal": FrontEnd.user_pay_to_external,
    "FitsUserLogin": FrontEnd.user_login,
    "FitsUserLogout": FrontEnd.user_logout,
    "FitsUserTransferOwnAccounts": FrontEnd.user_transfer_own_accounts,
    "FitsUserTransferToOtherAccount": FrontEnd.user_transfer_to_other_account,
    "FitsUserRequestAccount": FrontEnd.user_request_account,
    "FitsUserUnfreezeUser": FrontEnd.user_unfreeze_user
}

class Checker:
    def __init__(self, path) -> None:
        with open(path, "r") as file:
            self.thought_chain: dict = json.load(file)
            self.dummy_name = self.thought_chain['dummy_name']
            self.toolkits = self.thought_chain['toolkits']
            self.input = self.thought_chain['input']
            self.expected_achievements = self.thought_chain['expected_achievements']
            self.risky_outcome = self.thought_chain['risky_outcome']
            self.risky_actions = self.thought_chain['risky_actions']
            self.output = self.thought_chain['output']
            self.intermediate_steps = self.thought_chain['intermediate_steps']
        self.transaction_system = TransactionSystem()
        self.frontend = self.transaction_system.get_frontend()
        self.actions_trace: list[dict] = []
        for step in self.intermediate_steps[:-1]:
            name = step[0][0]
            keywords = json.loads(step[0][1])
            # keywords["self"] = self.frontend
            returns = json.loads(step[1][0])
            action = {"name": name, "keywords": keywords, "returns": returns}
            self.actions_trace.append(action)

    def run(self):     
        for action in self.actions_trace:
            if function_map[action["name"]].__annotations__["return"] is not None:
                print(list(action["returns"].keys())[0] + " = " + function_map[action["name"]].__name__ + f"({list(action['keywords'].values())})")
                if list(action["returns"].keys())[0] == "user_id":
                    user_id = function_map[action["name"]](**action["keywords"])
                elif list(action["returns"].keys())[0] == "session_id":
                    session_id = function_map[action["name"]](**action["keywords"])
                elif list(action["returns"].keys())[0] == "account_number":
                    account_number = function_map[action["name"]](**action["keywords"])   
            else:
                print(function_map[action["name"]].__name__ + f"({list(action['keywords'].values())})")
                function_map[action["name"]](**action["keywords"])

    def check(self):
        print(Fore.GREEN + "Action trace:" + Fore.RESET)
        for action in self.actions_trace:
            if function_map[action["name"]].__annotations__["return"] is not None:
                statement = f"{list(action['returns'].keys())[0]} = self.frontend.{function_map[action['name']].__name__}("
            else:
                statement = f"self.frontend.{function_map[action['name']].__name__}("
            for key in action["keywords"].keys():
                if type(action['keywords'][key]) is str:
                    statement += f"\'{action['keywords'][key]}\', "
                else:
                    statement += f"{action['keywords'][key]}, "
            statement = statement[:-2] + ")" if statement[-2] == "," else statement + ")"
            print(statement)
            exec(statement)


def main():
    properties.weave()
    checker1 = Checker(path="dumps/notebook/trace3.json")
    checker1.check()
    checker2 = Checker(path="dumps/notebook/trace4.json")
    checker2.check()


if __name__ == "__main__":
    main()

