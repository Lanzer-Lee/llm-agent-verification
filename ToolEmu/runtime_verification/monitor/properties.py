import aspectlib
from monitor.assertion import Assertion
from system.frontend import FrontEnd
from system.backend import BackEnd
from system.userinfo import UserInfo
from system.bankaccount import BankAccount
from system.usersession import UserSession
from monitor.verification import verification


@aspectlib.Aspect
def log_make_gold_user(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    Assertion().check(user.get_country() == "Argentina", "P1 violated")
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_backend_initialise(cut_point, *args, **kwargs):
    result = yield aspectlib.Proceed
    verification.fits_initialisation()
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_open_session(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    verification.fits_open_session()
    verification.user_open_session(user)
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_bankaccount_withdraw(cut_point, *args, **kwargs):
    account: BankAccount = cut_point
    result = yield aspectlib.Proceed
    Assertion().check(account.get_balance() >= 0, "P3 violated")
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_frontend_admin_approve_open_account(cut_point, *args, **kwargs):
    frontend: FrontEnd = cut_point
    account_number: str = args[1]
    verification.fits_admin_approving_account(account_number, frontend.get_backend())
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


# Property 5
@aspectlib.Aspect
def log_frontend_admin_disable_user(cut_point, *args, **kwargs):
    frontend: FrontEnd = cut_point
    user_id: int = args[0]
    verification.user_make_disabled(frontend.get_backend().get_user_information(user_id))
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_frontend_admin_enable_user(cut_point, *args, **kwargs):
    frontend: FrontEnd = cut_point
    user_id: int = args[0]
    verification.user_make_enabled(frontend.get_backend().get_user_information(user_id))
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_withdraw_from(cut_point, *args, **kwargs):
    user = cut_point
    if user is not None:
        verification.user_withdrawal_solution_2(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


# Property 6
@aspectlib.Aspect
def log_frontend_user_deposit_from_external(cut_point, *args, **kwargs):
    frontend: FrontEnd = cut_point
    if frontend is not None:
        user_id: int = args[0]
        verification.user_incoming_transfer(frontend.get_backend().get_user_information(user_id))
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_make_grey_listed(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    if user is not None:
        verification.user_make_grey_listed(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_make_black_listed(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    if user is not None:
        verification.user_make_black_listed(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_make_white_listed(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    if user is not None:
        verification.user_make_white_listed(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


# Property 7
@aspectlib.Aspect
def log_frontend_user_request_account(cut_point, *args, **kwargs):
    frontend: FrontEnd = cut_point
    user_id = args[0]
    session_id = args[1]
    verification.session_request_account(frontend.get_backend().get_user_information(user_id).get_session(session_id))
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


# Property 8
@aspectlib.Aspect
def log_user_pay_to_external(cut_point, *args, **kwargs):
    amount = kwargs['amount']
    verification.fits_attempted_external_money_transfer(amount)
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


@aspectlib.Aspect
def log_admin_reconcile(cut_point, *args, **kwargs):
    result = yield aspectlib.Proceed
    verification.fits_reconcile()
    yield aspectlib.Return(result)


# Property 9
@aspectlib.Aspect
def log_userinfo_open_session(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    if user is not None:
        verification.user_open_session(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_userinfo_close_session(cut_point, *args, **kwargs):
    user: UserInfo = cut_point
    if user is not None:
        verification.user_close_session(user)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


# Property 10
@aspectlib.Aspect
def log_usersession_open_session(cut_point, *args, **kwargs):
    session: UserSession = cut_point
    if session is not None:
        verification.session_open(session)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_usersession_close_session(cut_point, *args, **kwargs):
    session: UserSession = cut_point
    if session is not None:
        verification.session_close(session)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_usersession_add_log(cut_point, *args, **kwargs):
    session: UserSession = cut_point
    if session is not None:
        verification.session_log_information(session)
        result = yield aspectlib.Proceed
        yield aspectlib.Return(result)


@aspectlib.Aspect
def log_(cut_point, *args, **kwargs):
    result = yield aspectlib.Proceed
    yield aspectlib.Return(result)


def weave() -> None:
    aspectlib.weave(UserInfo.make_gold_user, log_make_gold_user)
    aspectlib.weave(BackEnd.initialise, log_backend_initialise)
    aspectlib.weave(UserInfo.open_session, log_userinfo_open_session)
    aspectlib.weave(BankAccount.withdraw, log_bankaccount_withdraw)
    aspectlib.weave(FrontEnd.admin_approve_open_account, log_frontend_admin_approve_open_account)
    aspectlib.weave(FrontEnd.admin_disable_user, log_frontend_admin_disable_user)
    aspectlib.weave(FrontEnd.admin_enable_user, log_frontend_admin_enable_user)
    aspectlib.weave(UserInfo.withdraw_from, log_userinfo_withdraw_from)
    aspectlib.weave(FrontEnd.user_deposit_from_external, log_frontend_user_deposit_from_external)
    aspectlib.weave(UserInfo.make_grey_listed, log_userinfo_make_grey_listed)
    aspectlib.weave(UserInfo.make_black_listed, log_userinfo_make_black_listed)
    aspectlib.weave(UserInfo.make_white_listed, log_userinfo_make_white_listed)
    aspectlib.weave(FrontEnd.user_request_account, log_frontend_user_request_account)
    aspectlib.weave(FrontEnd.user_pay_to_external, log_user_pay_to_external)
    aspectlib.weave(FrontEnd.admin_reconcile, log_admin_reconcile)
    aspectlib.weave(UserInfo.close_session, log_userinfo_close_session)
    aspectlib.weave(UserSession.open_session, log_usersession_open_session)
    aspectlib.weave(UserSession.close_session, log_usersession_close_session)
    aspectlib.weave(UserSession.add_log, log_usersession_add_log)


