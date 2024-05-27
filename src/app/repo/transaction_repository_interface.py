from abc import ABC, abstractmethod
from typing import List, Optional
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.entities.transaction import Transaction

class ITransactionRepository(ABC):
    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        '''
        Returns all the transactions in the database.
        '''
        pass
    
    @abstractmethod
    def get_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float) -> Optional[Transaction]:
        '''
        Returns the transaction with the given type, value, and timestamp.
        If the transaction does not exist, returns None.
        '''
        pass

    @abstractmethod
    def create_transaction(self, transaction: Transaction) -> Transaction:
        '''
        Creates a new transaction in the database and returns the created transaction.
        '''
        pass
    
    @abstractmethod
    def delete_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float) -> Optional[Transaction]:
        '''
        Deletes the transaction with the given type, value, and timestamp.
        If the transaction does not exist, returns None.
        '''
        pass

    @abstractmethod
    def update_transaction(self, transaction_type: TransactionTypeEnum, value: float, timestamp: float, new_transaction: Transaction) -> Optional[Transaction]:
        '''
        Updates the transaction with the given type, value, and timestamp with the new transaction data.
        If the transaction does not exist, returns None.
        '''
        pass
