from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

# from ..enums.item_type_enum import ItemTypeEnum

from ..entities.history import History

class IHistoryRepository(ABC):

    @abstractmethod
    def get_history(self) -> List[History]:
        """
        Returns the list of all transactions in the history.
        """
        pass