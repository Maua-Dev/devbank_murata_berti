from typing import Dict
from ..errors.entity_errors import ParamNotValidated

class Withdraw: 
    def __init__(self,current_balance: float = None, timestamp: float = None):
        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "must be a float")
        self.current_balance = current_balance

        if not self.validate_timestamp(timestamp):
            raise ParamNotValidated("timestamp", "must be a float")
        self.timestamp = timestamp

    @staticmethod
    def validate_current_balance(current_balance) -> bool:
        return isinstance(current_balance, float)
    
    @staticmethod
    def validate_timestamp(timestamp) -> bool:
        return isinstance(timestamp, float)
