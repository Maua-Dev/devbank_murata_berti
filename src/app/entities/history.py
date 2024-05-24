from typing import Dict
from ..errors.entity_errors import ParamNotValidated
from ..enums.item_type_enum import HistoryTypeEnum

class History: 
    def __init__(self, current_balance: float = None, timestamp: float = None, value: float = None, type: HistoryTypeEnum = None):
        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "must be a float")
        self.current_balance = current_balance

        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "must be a float")
        self.timestamp = timestamp

        if not self.validate_value(value):
            raise ParamNotValidated("value", "must be a float")
        self.value = value

        self.type = type

    @staticmethod
    def validate_current_balance(current_balance) -> bool:
        return isinstance(current_balance, float)
    
    @staticmethod
    def validate_timestamp(timestamp) -> bool:
        return isinstance(timestamp, float)
    
    @staticmethod
    def validate_value(value) -> bool:
        return isinstance(value, float)