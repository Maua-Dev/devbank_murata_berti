from typing import Dict

from src.app.enums.transaction_type_enum import TransactionTypeEnum
from ..errors.entity_errors import ParamNotValidated

class Transaction:
    current_balance: float
    timestamp: float
    value: float
    type: TransactionTypeEnum
     
    def __init__(self, current_balance: float = None, timestamp: float = None, value: float = None, type: TransactionTypeEnum = None):
        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "must be a float")
        self.current_balance = current_balance

        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "must be a float")
        self.timestamp = timestamp

        if not self.validate_value(value):
            raise ParamNotValidated("value", "must be a float")
        self.value = value

        if not self.validate_type(type):
            raise ParamNotValidated("type", "must be a valid HistoryTypeEnum")
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
    
    @staticmethod
    def validate_type(type) -> bool:
        return isinstance(type, TransactionTypeEnum)