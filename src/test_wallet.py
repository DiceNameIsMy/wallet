from accounts import Account
from wallet import Wallet


def test_get_account_by_name() -> None:
    account_1_name = "Card Account"
    account_1 = Account(name=account_1_name)
    wallet = Wallet(accounts=[account_1])

    assert wallet.get_account_by_name("invalid_account_name") is None
    assert wallet.get_account_by_name(account_1_name) is not None
