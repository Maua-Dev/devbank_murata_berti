from typing import List, Optional
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_interface import ITransactionRepository

class TransactionRepositoryMocky(ITransactionRepository):
    def __init__(self):
        self.transactions = [
            Transaction(current_balance=1000000000.0, timestamp=1000000000.0, value=1000000000.0, type=TransactionTypeEnum.DEPOSIT),
        ]

    def get_all_transactions(self) -> List[Transaction]:
        return self.transactions

    def get_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float) -> Optional[Transaction]:
        for transaction in self.transactions:
            if transaction.type == transaction_type and transaction.value == value and transaction.timestamp == timestamp:
                return transaction
        return None

    def create_transaction(self, transaction: Transaction) -> Transaction:
        self.transactions.append(transaction)
        return transaction

    def delete_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float) -> Optional[Transaction]:
        for idx, transaction in enumerate(self.transactions):
            if transaction.type == transaction_type and transaction.value == value and transaction.timestamp == timestamp:
                return self.transactions.pop(idx)
        return None

    def update_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float, new_transaction: Transaction) -> Optional[Transaction]:
        for idx, transaction in enumerate(self.transactions):
            if transaction.type == transaction_type and transaction.value == value and transaction.timestamp == timestamp:
                self.transactions[idx] = new_transaction
                return new_transaction
        return None