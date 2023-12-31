from __future__ import annotations

from decimal import Decimal
from typing import Self

from pydantic import Field

from base import BaseModel


class Amount(BaseModel):
    value: Decimal = Field(gt=0, decimal_places=2)

    @classmethod
    def new(cls, value: Decimal) -> Self:
        return cls(value=value)

    def negated(self) -> Decimal:
        return -self.value
