import pytest
from src.app.entities.user import User
from src.app.repo.user_repository_mock import UserRepositoryMocky

class Test_UserRepositoryMock:
    def test_get_all_users(self):
        repo = UserRepositoryMocky()
        
        users = repo.get_all_users()
        
        expected_users = repo.users
        
        assert expected_users == users

    def test_get_user(self):
        repo = UserRepositoryMocky()
        
        user = repo.get_user("Vini", "1234", "56789-0")
        
        expected_user = repo.users[0]
        
        assert expected_user == user

        non_existent_user = repo.get_user("Murata", "5678", "12345-6")
        assert non_existent_user is None

    def test_create_user(self):
        repo = UserRepositoryMocky()
        
        new_user = User(name="Murata", agency="5678", account="12345-6", current_balance=500.0)
        created_user = repo.create_user(new_user)
        
        assert created_user == new_user
        assert repo.get_user("Murata", "5678", "12345-6") == new_user

    def test_delete_user(self):
        repo = UserRepositoryMocky()
        
        deleted_user = repo.delete_user("Vini", "1234", "56789-0")
        
        assert deleted_user.name == "Vini"
        assert repo.get_user("Vini", "1234", "56789-0") is None

        non_existent_user_deletion = repo.delete_user("Murata", "5678", "12345-6")
        assert non_existent_user_deletion is None

    def test_update_user(self):
        repo = UserRepositoryMocky()
        
        updated_user = repo.update_user("Vini", "1234", "56789-0", 2000000000.0)
        
        assert updated_user is not None
        assert updated_user.current_balance == 2000000000.0
        
        non_existent_user_update = repo.update_user("Murata", "5678", "12345-6", 300.0)
        assert non_existent_user_update is None


# class Test_ItemRepositoryMock:
#     def test_get_all_items(self):
#         repo = ItemRepositoryMock()
#         assert all([item_expect == item for item_expect, item in zip(repo.items.values(), repo.get_all_items())]) 
        
#     def test_get_item(self):
#         repo = ItemRepositoryMock()
#         item = repo.get_item(item_id=1)
#         assert item == repo.items.get(1)
    
#     def test_get_item_not_found(self):
#         repo = ItemRepositoryMock()
#         item = repo.get_item(item_id=10)
#         assert item is None
        
#     def test_create_item(self):
#         repo = ItemRepositoryMock()
#         len_before = len(repo.items)
#         item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
#         repo.create_item(item=item, item_id=0)
#         len_after = len(repo.items)
#         assert len_after == len_before + 1
#         assert repo.items.get(0) == item
        
#     def test_delete_item(self):
#         repo = ItemRepositoryMock()
#         item_expected_to_be_deleted = repo.items.get(1)
#         len_before = len(repo.items)
        
#         item = repo.delete_item(item_id=1)
#         len_after = len(repo.items)
#         assert len_after == len_before - 1
#         assert item == item_expected_to_be_deleted
        
#     def test_delete_item_not_found(self):
#         repo = ItemRepositoryMock()
#         item = repo.delete_item(item_id=10)
#         assert item is None
        
#     def test_update_item(self):
#         repo = ItemRepositoryMock()
#         item = Item(name="test", price=1.0, item_type=ItemTypeEnum.TOY, admin_permission=False)
#         item_updated = repo.update_item(item_id=1, name=item.name, price=item.price, item_type=item.item_type, admin_permission=item.admin_permission)
        
#         assert item_updated == item
#         assert repo.items.get(1) == item
        
#     def test_update_item_partial_1(self):
#         repo = ItemRepositoryMock()
#         name = "test"
#         item_updated = repo.update_item(item_id=1, name=name)
        
#         assert item_updated.name == name
#         assert repo.items.get(1).name == name
        
#     def test_update_item_partial_2(self):
#         repo = ItemRepositoryMock()
#         price = 1.0
#         item_updated = repo.update_item(item_id=1, price=price)
        
#         assert item_updated.price == price
#         assert repo.items.get(1).price == price