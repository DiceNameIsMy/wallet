from __future__ import annotations

from decimal import Decimal
from typing import Optional, Self

from pydantic import Field

from base import BaseModel
from operations.tags import Tag
from operations.types import Amount, ExpenceType, IncomeType, Type


class Operation(BaseModel):
    type: Type
    amount: Amount
    tags: list[Tag] = Field(default_factory=list)

    @classmethod
    def new_income(
        cls, amount: Amount, tags: Optional[list[Tag]] = None
    ) -> Self:
        return cls(type=IncomeType(), amount=amount, tags=tags or [])

    @classmethod
    def new_expence(
        cls, amount: Amount, tags: Optional[list[Tag]] = None
    ) -> Self:
        return cls(type=ExpenceType(), amount=amount, tags=tags or [])

    def shift(self) -> Decimal:
        return self.type.apply_shift(self.amount)
