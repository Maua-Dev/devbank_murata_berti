from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

# from ..enums.item_type_enum import ItemTypeEnum

from ..entities.transaction import Transaction

class ITransactionRepository(ABC):

    @abstractmethod
    def get_all_transaction(self) -> List[Transaction]:
        """
        Returns all the itens in the database 
        """
        pass
