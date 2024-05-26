import pytest
# from src.app.entities.item import Item
# from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

from src.app.entities.transaction import Transaction


class Test_History:
    def test_history(self):
        current_balance = 1000000000.0
        timestamp = 1000000000.0
        value = 1000000000.0
        type = TransactionTypeEnum.deposit

        item = Transaction(current_balance = current_balance, timestamp = timestamp, value = value, type = type)
    
        assert item.current_balance == 1000000000.0
        assert item.timestamp == 1000000000.0
        assert item.value == 1000000000.0
        assert item.type == TransactionTypeEnum.deposit

    def test_current_balance(self):
        with pytest.raises(ParamNotValidated):
            item = Transaction(current_balance = 1000000000, timestamp = 1000000000.0, value = 1000000000.0, type = TransactionTypeEnum.deposit)

    def test_timestamp(self):
        with pytest.raises(ParamNotValidated):
            item = Transaction(current_balance = 1000000000.0, timestamp = 1000000000, value = 1000000000.0, type = TransactionTypeEnum.deposit)

    def test_value(self):
        with pytest.raises(ParamNotValidated):
            item = Transaction(current_balance = 1000000000.0, timestamp = 1000000000.0, value = 1000000000, type = TransactionTypeEnum.deposit)

    def test_type(self):
        with pytest.raises(ParamNotValidated):
            item = Transaction(current_balance = 1000000000.0, timestamp = 1000000000.0, value = 1000000000, type = "deposit")