import pytest
from src.app.errors.entity_errors import ParamNotValidated

from src.app.entities.item import Withdraw


class Test_Withdraw:
    def test_deposit(self):
        current_balance = 1000000000.0
        timestamp = 1000000000.0

        item = Withdraw( current_balance = current_balance, timestamp = timestamp)
    
        assert item.current_balance == 1000000000.0
        assert item.timestamp == 1000000000.0

    def test_current_balance(self):
        with pytest.raises(ParamNotValidated):
            item = Withdraw(current_balance = 1000000000, timestamp = 1000000000.0)

    def test_timestamp(self):
        with pytest.raises(ParamNotValidated):
            item = Withdraw(current_balance = 1000000000.0, timestamp = 1000000000)