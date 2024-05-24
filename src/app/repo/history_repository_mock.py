from typing import Dict, Optional, List
from ..entities.history import History
from ..repo.history_repository_interface import IHistoryRepository

class HistoryRepositoryMocky(IHistoryRepository):
    history: List[History]

    def __init__(self):
        self.history = [
            History(current_balance = 1000000000.0, timestamp= 1000000000.0, value= 1000000000.0, type= "deposit"),
        ]

    def get_history(self) -> List[History]:
        return self.items