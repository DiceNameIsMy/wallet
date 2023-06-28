from __future__ import annotations

from decimal import Decimal

from pydantic import Field

from base import BaseModel
from operations.currencies import Currency
from operations.operations import Operation
from operations.tags import Tag


class Account(BaseModel):
    name: str
    currency: Currency
    operations: list[Operation] = Field(default=list)

    def add_operation(self, operation: Operation) -> None:
        self.operations.append(operation)

    def get_operations(self) -> list[Operation]:
        return self.operations

    def get_operations_by_tag(self, tag: Tag) -> list[Operation]:
        return [op for op in self.operations if tag in op.tags]

    def balance(self) -> Decimal:
        balance = Decimal("0.00")
        for op in self.operations:
            balance += op.shift()
        return balance
