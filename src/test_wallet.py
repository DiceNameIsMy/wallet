from decimal import Decimal

import pytest

from accounts import Account
from operations.amount import Amount
from operations.currencies import Currency
from operations.tags import Tag
from wallet import AccountNamesNotUnique, Wallet


class TestInitialization:
    def test_valid(self) -> None:
        account_1 = Account(name="account_name_1", currency=Currency.USD)
        account_2 = Account(name="account_name_2", currency=Currency.USD)

        Wallet(accounts=[account_1, account_2])

    def test_with_same_account_names(self) -> None:
        account_1 = Account(name="same_name", currency=Currency.USD)
        account_2 = Account(name="same_name", currency=Currency.USD)
        with pytest.raises(AccountNamesNotUnique):
            Wallet(accounts=[account_1, account_2])


def test_get_account_by_name(wallet: Wallet, account: Account) -> None:
    assert wallet.get_account_by_name("invalid_account_name") is None
    assert wallet.get_account_by_name(account.name) is not None


class TestTransfer:
    def test_same_currencies(
        self, wallet: Wallet, account: Account, second_account: Account
    ) -> None:
        wallet.send_transfer(
            sender=account,
            sender_amount=Amount.new(Decimal("10.50")),
            receiver=second_account,
            receiver_amount=Amount.new(Decimal("10.50")),
        )

        transfers = wallet.get_transfers()
        assert len(transfers) == 1

        transfer = transfers[0]
        assert transfer.sender_name == account.name
        assert transfer.sender_amount == Amount.new(Decimal("10.50"))
        assert transfer.receiver_name == second_account.name
        assert transfer.receiver_amount == Amount.new(Decimal("10.50"))

        assert account.balance() == Decimal("-10.50")
        assert len(account.get_operations_by_tag(Tag.tranfser())) == 1

        assert second_account.balance() == Decimal("10.50")
        assert len(second_account.get_operations_by_tag(Tag.tranfser())) == 1

    def test_different_currencies(
        self,
        wallet: Wallet,
        account: Account,
        different_currency_account: Account,
    ) -> None:
        wallet.send_transfer(
            sender=account,
            sender_amount=Amount.new(Decimal("10.50")),
            receiver=different_currency_account,
            receiver_amount=Amount.new(Decimal("9.00")),
        )

        transfers = wallet.get_transfers()
        assert len(transfers) == 1

        transfer = transfers[0]
        assert transfer.sender_name == account.name
        assert transfer.sender_amount == Amount.new(Decimal("10.50"))
        assert transfer.receiver_name == different_currency_account.name
        assert transfer.receiver_amount == Amount.new(Decimal("9.00"))

        assert account.balance() == Decimal("-10.50")
        assert len(account.get_operations_by_tag(Tag.tranfser())) == 1

        assert different_currency_account.balance() == Decimal("9.00")
        different_currency_account_transfers = (
            different_currency_account.get_operations_by_tag(Tag.tranfser())
        )
        assert len(different_currency_account_transfers) == 1
