from typing import Optional

from accounts import Account
from base import BaseModel
from operations.amount import Amount
from operations.operations import Operation
from operations.tags import Tag


class Transfer(BaseModel):
    sender_name: str
    sender_amount: Amount
    receiver_name: str
    receiver_amount: Amount


class AccountNamesNotUnique(Exception):
    pass


class WalletValidator:
    def validate_accounts_names_unique(self, accounts: list[Account]) -> None:
        accounts_names = list(map(lambda a: a.name, accounts))
        unique_accounts_names = set(accounts_names)
        if len(accounts_names) != len(unique_accounts_names):
            raise AccountNamesNotUnique()


class Wallet:
    accounts: list[Account]
    transfers: list[Transfer]
    _validators = WalletValidator()

    def __init__(
        self,
        *,
        accounts: Optional[list[Account]] = None,
        transfers: Optional[list[Transfer]] = None
    ) -> None:
        self.accounts = accounts or []
        self.transfers = transfers or []

        self._validators.validate_accounts_names_unique(self.accounts)

    def get_account_by_name(self, name: str) -> Optional[Account]:
        for account in self.accounts:
            if account.name == name:
                return account
        return None

    def get_accounts(self) -> list[Account]:
        return self.accounts

    def get_transfers(self) -> list[Transfer]:
        return self.transfers

    def send_transfer(
        self,
        sender: Account,
        sender_amount: Amount,
        receiver: Account,
        receiver_amount: Amount,
    ) -> None:
        sender.add_operation(
            Operation.new_expence(sender_amount, tags=[Tag.tranfser()])
        )
        receiver.add_operation(
            Operation.new_income(receiver_amount, tags=[Tag.tranfser()])
        )
        self._add_transfer(
            sender.name, sender_amount, receiver.name, receiver_amount
        )

    def _add_transfer(
        self,
        sender_name: str,
        sender_amount: Amount,
        receiver_name: str,
        receiver_amount: Amount,
    ) -> None:
        self.transfers.append(
            Transfer(
                sender_name=sender_name,
                sender_amount=sender_amount,
                receiver_name=receiver_name,
                receiver_amount=receiver_amount,
            )
        )
