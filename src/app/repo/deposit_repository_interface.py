from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

# from ..enums.item_type_enum import ItemTypeEnum

from ..entities.deposit import Deposit

class IDepositRepository(ABC):

    @abstractmethod
    def get_deposit_balance(self) -> float:
        """
        Returns the current balance of the user.
        """
        pass

    @abstractmethod
    def update_deposit_balance(self, new_balance: float) -> None:
        """
        Updates the balance of the user.
        """
        pass