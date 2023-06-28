from decimal import Decimal

from accounts import Account
from operations.currencies import Currency
from operations.operations import Operation
from operations.tags import Tag
from operations.types import Amount


def test_balance(account: Account) -> None:
    expence_operation = Operation.new_income(Amount.new(Decimal("100.00")))
    income_operation = Operation.new_expence(Amount.new(Decimal("50.50")))
    account = Account(
        name="",
        currency=Currency.USD,
        operations=[income_operation, expence_operation],
    )

    assert account.balance() == Decimal("49.50")


def test_operation(account: Account) -> None:
    account.add_operation(Operation.new_income(Amount.new(Decimal("100.00"))))
    account.add_operation(Operation.new_expence(Amount.new(Decimal("50.50"))))

    assert account.balance() == Decimal("49.50")


class TestGetOperationsByTag:
    def test_has_operations(self, account: Account) -> None:
        tag = Tag(name="Shopping")
        account.add_operation(
            Operation.new_expence(Amount.new(Decimal("50.50")), tags=[tag])
        )

        found_operations = account.get_operations_by_tag(tag)
        assert len(found_operations) == 1

        assert tag in found_operations[0].tags

    def test_no_match(self, account: Account) -> None:
        account.add_operation(
            Operation.new_expence(
                Amount.new(Decimal("50.50")), tags=[Tag(name="Casino")]
            )
        )

        found_operations = account.get_operations_by_tag(Tag(name="Shopping"))
        assert len(found_operations) == 0
