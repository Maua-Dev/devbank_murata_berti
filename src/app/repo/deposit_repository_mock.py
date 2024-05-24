from typing import Dict, Optional, List
from ..entities.deposit import Deposit
from ..repo.deposit_repository_interface import IDepositRepository

class DepositRepositoryMocky(IDepositRepository):
    deposit: List[Deposit]

    def __init__(self):
        self.deposit = [
            Deposit(current_balance = 1000000000.0, timestamp= 1000000000.0),
        ]

    def get_deposit_balance(self) -> float:
        return self.deposit[-1].current_balance

    def update_deposit_balance(self, new_balance: float) -> None:
        self.deposit.append(Deposit(current_balance=new_balance, timestamp=1000000000.0))