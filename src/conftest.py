import pytest

from accounts import Account
from operations.currencies import Currency
from wallet import Wallet


@pytest.fixture()
def wallet(
    account: Account,
    second_account: Account,
    different_currency_account: Account,
) -> Wallet:
    """
    Wallet account with 2 USD and 1 EUR accounts
    """
    return Wallet(
        accounts=[account, second_account, different_currency_account]
    )


@pytest.fixture()
def account() -> Account:
    return Account(name="account", currency=Currency.USD, operations=[])


@pytest.fixture()
def second_account() -> Account:
    return Account(name="second_account", currency=Currency.USD, operations=[])


@pytest.fixture()
def different_currency_account() -> Account:
    return Account(
        name="different_currency_account", currency=Currency.EUR, operations=[]
    )
