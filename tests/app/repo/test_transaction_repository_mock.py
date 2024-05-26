import pytest
# from src.app.entities.item import Item
# from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.repo.user_repository_mock import UserRepositoryMocky

class Test_UserRepositoryMock:
    def test_get_all_items(self):
        repo = UserRepositoryMocky()

        items = repo.get_all_items()

        expected_item = repo.items

        assert expected_item == items