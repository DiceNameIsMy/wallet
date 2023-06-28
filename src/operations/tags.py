from __future__ import annotations

from typing import Self

from base import BaseModel


class Tag(BaseModel):
    name: str

    @classmethod
    def tranfser(cls) -> Self:
        return cls(name="Transfer")

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Tag):
            return self.name == __value.name
        return False
