from typing import List, Optional
from src.app.entities.user import User
from src.app.repo.user_repository_interface import IUserRepository

class UserRepositoryMocky(IUserRepository):
    def __init__(self):
        self.users = [
            User(name="Vini", agency="1234", account="56789-0", current_balance=1000000000.0),
        ]

    def get_all_users(self) -> List[User]:
        return self.users

    def get_user(self, name: str, agency: str, account: str) -> Optional[User]:
        for user in self.users:
            if user.name == name and user.agency == agency and user.account == account:
                return user
        return None

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def delete_user(self, name: str, agency: str, account: str) -> Optional[User]:
        for idx, user in enumerate(self.users):
            if user.name == name and user.agency == agency and user.account == account:
                return self.users.pop(idx)
        return None

    def update_user(self, name: str, agency: str, account: str, current_balance: float) -> Optional[User]:
        for user in self.users:
            if user.name == name and user.agency == agency and user.account == account:
                user.current_balance = current_balance
                return user
        return None
     
# class ItemRepositoryMock(IItemRepository):
#     items: Dict[int, Item]
    
#     def __init__(self):
#         self.items = {
#             1: Item(name="Barbie", price=48.90, item_type=ItemTypeEnum.TOY, admin_permission=False),
#             2: Item(name="Hamburguer", price=38.00, item_type=ItemTypeEnum.FOOD, admin_permission=False),
#             3: Item(name="T-shirt", price=22.95, item_type=ItemTypeEnum.CLOTHES, admin_permission=False),
#             4: Item(name="Super Mario Bros", price=55.00, item_type=ItemTypeEnum.GAMES, admin_permission=True)
#         }
        
#     def get_all_items(self) -> List[Item]:
#         return self.items.values()
    
#     def get_item(self, item_id: int) -> Optional[Item]:
#         return self.items.get(item_id, None)
    
#     def create_item(self, item: Item, item_id: int) -> Item:
        
#         self.items[item_id] = item
#         return item
    
#     def delete_item(self, item_id: int) -> Item:
#         item = self.items.pop(item_id, None)
#         return item
        
        
#     def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#         item = self.items.get(item_id, None)
#         if item is None:
#             return None
        
#         if name is not None:
#             item.name = name
#         if price is not None:
#             item.price = price
#         if item_type is not None:
#             item.item_type = item_type
#         if admin_permission is not None:
#             item.admin_permission = admin_permission
#         self.items[item_id] = item
        
#         return item
        
    
    