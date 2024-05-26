import pytest
# from src.app.entities.item import Item
# from src.app.enums.item_type_enum import ItemTypeEnum
from src.app.errors.entity_errors import ParamNotValidated

from src.app.entities.user import User


class Test_User:
    def test_user(self):
        name = "Vini"
        agency = "1234"
        account = "56789-0"
        current_balance = 1000000000.0

        item = User(name, agency = agency, account = account, current_balance = current_balance)
    
        assert item.name == "Vini"
        assert item.agency == "1234"
        assert item.account == "56789-0"
        assert item.current_balance == 1000000000.0

    def test_agency_wrong(self):
        with pytest.raises(ParamNotValidated):
            item = User(name = "Vini", agency = "12346", account = "56789-0", current_balance = 1000000000.0)
            
    def test_account_wrong(self):
        with pytest.raises(ParamNotValidated):
            item = User(name = "Vini", agency = "1234", account = "567892", current_balance = 1000000000.0)

    def test_current_balance(self):
        with pytest.raises(ParamNotValidated):
            item = User(name = "Vini", agency = "1234", account = "5678-9", current_balance = 1000000000)

    def test_to_dict(self):
        name = "Vini"
        agency = "1234"
        account = "56789-0"
        current_balance = 1000000000.0

        item = User(name, agency = agency, account = account, current_balance = current_balance)

        item_dict = item.to_dict()

        expected_item_dict = {
            "name": name,
            "agency": agency,
            "account": account,
            "current_balance": current_balance,
        }

        assert item_dict == expected_item_dict


# class Test_Item:
#     def test_item(self):
#         item = Item("test", 1.0, ItemTypeEnum.FOOD, admin_permission=True)
#         assert item.name == "test"
#         assert item.price == 1.0
#         assert item.item_type == ItemTypeEnum.FOOD
        
#     def test_item_dict(self):
#         item = Item("test", 1.0, ItemTypeEnum.FOOD, admin_permission=True)
#         assert item.to_dict() == {'admin_permission': True, 'item_type': 'FOOD', 'name': 'test', 'price': 1.0}
    
#     def test_item_name_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_name_is_not_string(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name=1.0, price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_name_is_too_short(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="te", price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_price_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_price_is_not_float(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price="1.0", item_type=ItemTypeEnum.FOOD, admin_permission=True)
#     def test_item_price_is_negative(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=-1.0, item_type=ItemTypeEnum.FOOD, admin_permission=True)
            
#     def test_item_type_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, admin_permission=True)
            
#     def test_item_type_is_not_enum(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type="FOOD", admin_permission=True)
            
#     def test_item_admin_permission_is_none(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type=ItemTypeEnum.FOOD)
        
#     def test_item_admin_permission_is_not_bool(self):
#         with pytest.raises(ParamNotValidated):
#             Item(name="test", price=1.0, item_type=ItemTypeEnum.FOOD, admin_permission="True")