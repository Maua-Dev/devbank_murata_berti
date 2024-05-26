from typing import Dict, Optional, List
from ..entities.transaction import Transaction
from ..repo.transaction_repository_interface import ITransactionRepository

class TransactionRepositoryMocky(ITransactionRepository):
    transaction: List[Transaction]

    def __init__(self):
        self.transaction = [
            Transaction(current_balance = 1000000000.0, timestamp= 1000000000.0, value= 1000000000.0, type= "deposit"),
        ]

    def get_transaction(self) -> List[Transaction]:
        return self.items