from typing import Dict
from ..errors.entity_errors import ParamNotValidated

class User: 
    name: str
    agency: str
    account: str
    current_balance: float
    
    def __init__(self, name: str = None, agency: str = None, account: str = None, current_balance: float = None):
        if not self.validate_name(name):
            raise ParamNotValidated("name", "must be a non-empty string")
        self.name = name

        if not self.validate_agency(agency):
            raise ParamNotValidated("agency", "must have 4 digits")
        self.agency = agency

        if not self.validate_account(account):
            raise ParamNotValidated("account", "must follow the following pattern XXXXX-X")
        self.account = account

        if not self.validate_current_balance(current_balance):
            raise ParamNotValidated("current_balance", "must be a float")
        self.current_balance = current_balance


    @staticmethod
    def validate_name(name) -> bool:
        return isinstance(name, str) and bool(name.strip())    

    @staticmethod
    def validate_agency(agency) -> bool:
        if agency is None or len(agency) != 4:
            return False
        return True
    
    @staticmethod
    def validate_account(account) -> bool:
        if account is None or len(account) != 7 or account[5] != '-':
            return False
        return True
    
    @staticmethod
    def validate_current_balance(current_balance) -> bool:
        return isinstance(current_balance, float)
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }
    
# class Item:
#     name: str
#     price: float
#     item_type: ItemTypeEnum
#     admin_permission: bool = False
    
#     def __init__(self, name: str=None, price: float=None, item_type: ItemTypeEnum=None, admin_permission: bool=None):
#         validation_name = self.validate_name(name)
#         if validation_name[0] is False:
#             raise ParamNotValidated("name", validation_name[1])
#         self.name = name
        
#         validation_price = self.validate_price(price)
#         if validation_price[0] is False:
#             raise ParamNotValidated("price", validation_price[1])
#         self.price = price

#         validation_item_type = self.validate_item_type(item_type)
#         if validation_item_type[0] is False:
#             raise ParamNotValidated("item_type", validation_item_type[1])
#         self.item_type = item_type
        
#         validation_admin_permission = self.validate_admin_permission(admin_permission)
#         if validation_admin_permission[0] is False:
#             raise ParamNotValidated("admin_permission", validation_admin_permission[1])
#         self.admin_permission = admin_permission
        
#     @staticmethod
#     def validate_name(name: str) -> Tuple[bool, str]:
#         if name is None:
#             return (False, "Name is required")
#         if type(name) != str:
#             return (False, "Name must be a string")
#         if len(name) < 3:
#             return (False, "Name must be at least 3 characters long")
#         return (True, "")
        
#     @staticmethod
#     def validate_price(price: float) -> Tuple[bool, str]:
#         if price is None:
#             return (False, "Price is required")
#         if type(price) != float:
#             return (False, "Price must be a float")
#         if price < 0:
#             return (False, "Price must be a positive number")
#         return (True, "")
    
#     @staticmethod
#     def validate_item_type(item_type: ItemTypeEnum) -> Tuple[bool, str]:
#         if item_type is None:
#             return (False, "Item type is required")
#         if type(item_type) != ItemTypeEnum:
#             return (False, "Item type must be a ItemTypeEnum")
#         return (True, "")
    
#     @staticmethod
#     def validate_admin_permission(admin_permission: bool) -> Tuple[bool, str]:
#         if admin_permission is None:
#             return (False, "Admin permission is required")
#         if type(admin_permission) != bool:
#             return (False, "Admin permission must be a boolean")
#         return (True, "")
        
#     @staticmethod
#     def validate_item_id(item_id: int) -> Tuple[bool, str]:
#         if item_id is None:
#             return (False, "Missing 'item_id' parameter")

#         if type(item_id) != int:
#             return (False, "Parameter 'item_id' must be an integer")
        
#         if item_id < 0:
#             return (False, "Parameter 'item_id' must be a positive integer")

#         return (True, "")
    
        
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "price": self.price,
#             "item_type": self.item_type.value,
#             "admin_permission": self.admin_permission
#         }
    
#     def __eq__(self,other):
#         return self.name == other.name and self.price == other.price and self.item_type == other.item_type and self.admin_permission == other.admin_permission
    
#     def __repr__(self):
#         return f"Item(name={self.name}, price={self.price}, item_type={self.item_type}, admin_permission={self.admin_permission})"