import pytest
# from src.app.entities.item import Item
# from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

from src.app.entities.item import History


class Test_History:
    def test_history(self):
        current_balance = 1000000000.0
        timestamp = 1000000000.0
        value = 1000000000.0
        type = ItemTypeEnum.deposit

        item = History(current_balance = current_balance, timestamp = timestamp, value = value, type = type)
    
        assert item.current_balance == 1000000000.0
        assert item.timestamp == 1000000000.0
        assert item.value == 1000000000.0
        assert item.type == ItemTypeEnum.deposit

    def test_current_balance(self):
        with pytest.raises(ParamNotValidated):
            item = History(current_balance = 1000000000, timestamp = 1000000000.0, value = 1000000000.0)

    def test_timestamp(self):
        with pytest.raises(ParamNotValidated):
            item = History(current_balance = 1000000000.0, timestamp = 1000000000.0, value = 1000000000.0)

    def test_value(self):
        with pytest.raises(ParamNotValidated):
            item = History(current_balance = 1000000000.0, timestamp = 1000000000.0, value = 1000000000)