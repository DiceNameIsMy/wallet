from decimal import Decimal

from accounts import Account
from operations.operations import Operation
from operations.tags import Tag
from operations.types import Amount


def new_account(operations: list[Operation]) -> Account:
    return Account(name="", operations=operations)


def test_balance() -> None:
    expence_operation = Operation.new_income(Amount.new(Decimal("100.00")))
    income_operation = Operation.new_expence(Amount.new(Decimal("50.50")))
    account = new_account(operations=[income_operation, expence_operation])

    assert account.balance() == Decimal("49.50")


def test_operation() -> None:
    account = new_account(operations=[])
    account.add_operation(Operation.new_income(Amount.new(Decimal("100.00"))))
    account.add_operation(Operation.new_expence(Amount.new(Decimal("50.50"))))

    assert account.balance() == Decimal("49.50")


def test_transfer() -> None:
    account = new_account(operations=[])
    second_account = new_account(operations=[])
    account.send_transfer(second_account, Amount(value=Decimal("10.50")))

    assert account.balance() == Decimal("-10.50")
    assert len(account.get_operations_by_tag(Tag.tranfser())) == 1

    assert second_account.balance() == Decimal("10.50")
    assert len(second_account.get_operations_by_tag(Tag.tranfser())) == 1


class TestGetOperationsByTag:
    def test_has_operations(self) -> None:
        tag = Tag(name="Shopping")
        operation = Operation.new_expence(
            Amount.new(Decimal("50.50")), tags=[tag]
        )
        account = new_account(operations=[operation])

        found_operations = account.get_operations_by_tag(tag)
        assert len(found_operations) == 1

        assert tag in found_operations[0].tags

    def test_no_match(self) -> None:
        account = new_account(
            operations=[
                Operation.new_expence(
                    Amount.new(Decimal("50.50")), tags=[Tag(name="Casino")]
                )
            ]
        )

        found_operations = account.get_operations_by_tag(Tag(name="Shopping"))
        assert len(found_operations) == 0
