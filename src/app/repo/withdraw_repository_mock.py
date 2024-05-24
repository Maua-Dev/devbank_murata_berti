from typing import Dict, Optional, List
from ..entities.withdraw import Withdraw
from ..repo.withdraw_repository_interface import IWithdrawRepository

class RepositoryMocky(IWithdrawRepository):
    withdraw: List[Withdraw]

    def __init__(self):
        self.items = [
            Withdraw(current_balance = 1000000000.0, timestamp= 1000000000.0),
        ]

    def get_withdraw_balance(self) -> float:
        return self.withdraw[-1].current_balance

    def update_withdraw_balance(self, new_balance: float) -> None:
        self.withdraw.append(Withdraw(current_balance=new_balance, timestamp=1000000000.0))