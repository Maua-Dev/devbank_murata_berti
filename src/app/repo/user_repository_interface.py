from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

# from ..enums.item_type_enum import ItemTypeEnum

from ..entities.user import User

class IUserRepository(ABC):

    @abstractmethod
    def get_all_users(self) -> List[User]:
        '''
        Returns all the users in the database.
        '''
        pass
    
    @abstractmethod
    def get_user(self, name: str, agency: str, account: str) -> Optional[User]:
        '''
        Returns the user with the given name, agency, and account.
        If the user does not exist, returns None.
        '''
        pass

    @abstractmethod
    def create_user(self, user: User) -> User:
        '''
        Creates a new user in the database and returns the created user.
        '''
        pass
    
    @abstractmethod
    def delete_user(self, name: str, agency: str, account: str) -> Optional[User]:
        '''
        Deletes the user with the given name, agency, and account.
        If the user does not exist, returns None.
        '''
        pass

    @abstractmethod
    def update_user(self, name: str, agency: str, account: str, current_balance: float) -> Optional[User]:
        '''
        Updates the user with the given name, agency, and account.
        If the user does not exist, returns None.
        '''
        pass
                        

# class IItemRepository(ABC):
    
    
#     @abstractmethod
#     def get_all_items(self) -> List[Item]:
#         '''
#         Returns all the itens in the database 
#         '''
#         pass
    
#     @abstractmethod
#     def get_item(self, item_id: int) -> Optional[Item]:
#         '''
#         Returns the item with the given id.
#         If the item does not exist, returns None
#         '''
#         pass
    
#     @abstractmethod
#     def create_item(self, item: Item, item_id: int) -> Item:
#         '''
#         Creates a new item in the database
#         '''
#         pass
    
#     @abstractmethod
#     def delete_item(self, item_id: int) -> Item:
#         '''
#         Deletes the item with the given id.
#         If the item does not exist, returns None
#         '''
        
#     @abstractmethod
#     def update_item(self, item_id:int, name:str=None, price:float=None, item_type:ItemTypeEnum=None, admin_permission:bool=None) -> Item:
#         '''
#         Updates the item with the given id.
#         If the item does not exist, returns None
#         '''
#         pass
    
    