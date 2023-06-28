from __future__ import annotations

import enum
from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Literal

from base import BaseModel
from operations.amount import Amount


class TypeEnum(enum.Enum):
    INCOME = "INCOME"
    EXPENCE = "EXPENCE"


class Type(ABC, BaseModel):
    enum: TypeEnum

    @abstractmethod
    def apply_shift(self, amount: Amount) -> Decimal:
        pass


class IncomeType(Type):
    enum: Literal[TypeEnum.INCOME] = TypeEnum.INCOME

    def apply_shift(self, amount: Amount) -> Decimal:
        return amount.value


class ExpenceType(Type):
    enum: Literal[TypeEnum.EXPENCE] = TypeEnum.EXPENCE

    def apply_shift(self, amount: Amount) -> Decimal:
        return amount.negated()
