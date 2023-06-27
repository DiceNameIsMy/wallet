from typing import Optional

from accounts import Account


class Wallet:
    accounts: list[Account]

    def __init__(self, *, accounts: Optional[list[Account]] = None) -> None:
        self.accounts = accounts or []

    def get_account_by_name(self, name: str) -> Optional[Account]:
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_accounts(self) -> list[Account]:
        return self.accounts
