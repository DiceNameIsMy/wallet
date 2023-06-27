from __future__ import annotations

from decimal import Decimal
from typing import Optional

from pydantic import Field

from base import BaseModel
from operations.amount import Amount
from operations.operations import Operation
from operations.tags import Tag


class Account(BaseModel):
    name: str
    operations: list[Operation] = Field(default=list)

    def add_operation(self, operation: Operation) -> None:
        self.operations.append(operation)

    def send_transfer(
        self, to: Account, amount: Amount, tags: Optional[list[Tag]] = None
    ) -> None:
        tags = tags or []
        tags.append(Tag.tranfser())
        self.add_operation(Operation.new_expence(amount, tags))

        to.receive_transfer(amount)

    def receive_transfer(
        self, amount: Amount, tags: Optional[list[Tag]] = None
    ) -> None:
        tags = tags or []
        tags.append(Tag.tranfser())
        self.add_operation(Operation.new_income(amount, [Tag.tranfser()]))

    def get_operations(self) -> list[Operation]:
        return self.operations

    def get_operations_by_tag(self, tag: Tag) -> list[Operation]:
        return [op for op in self.operations if tag in op.tags]

    def balance(self) -> Decimal:
        balance = Decimal("0.00")
        for op in self.operations:
            balance += op.shift()
        return balance
