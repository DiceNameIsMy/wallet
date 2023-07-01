import enum


class Currency(enum.Enum):
    USD = "USD"
    EUR = "EUR"
    CZK = "CZK"
    KZT = "KZT"

    @property
    def abbreviation(self) -> str:
        return self.value
