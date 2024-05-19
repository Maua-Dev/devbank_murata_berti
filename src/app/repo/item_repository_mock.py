from typing import Dict, Optional, List

# from ..enums.item_type_enum import ItemTypeEnum
from ..entities.item import Item
from ..repo.item_repository_interface import IItemRepository

class ItemRepositoryMocky(IItemRepository):
    items: List[Item]

    def __init__(self):
        self.items = [
            Item(name = "Vini", agency = "1234", account = "56789-0", current_balance = 1000000000.0),
            Item(name = "Vini2", agency = "4321", account = "09876-5", current_balance = 10000000000.0),
            Item(name = "Vini3", agency = "2143", account = "76509-8", current_balance = 10000000000.0)
        ]

    def get_all_items(self) -> List[Item]:
        return self.items
     
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
        
    
    