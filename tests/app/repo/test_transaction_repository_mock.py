import pytest
from src.app.entities.transaction import Transaction
from src.app.enums.transaction_type_enum import TransactionTypeEnum
from src.app.repo.transaction_repository_mock import TransactionRepositoryMocky

class Test_TransactionRepositoryMock:
    def test_get_all_transactions(self):
        repo = TransactionRepositoryMocky()
        
        transactions = repo.get_all_transactions()
        
        expected_transactions = repo.transactions
        
        assert expected_transactions == transactions

    def test_get_transaction(self):
        repo = TransactionRepositoryMocky()
        
        transaction = repo.get_transaction(TransactionTypeEnum.DEPOSIT, 1000000000.0, 1000000000.0)
        
        expected_transaction = repo.transactions[0]
        
        assert expected_transaction == transaction

        non_existent_transaction = repo.get_transaction(TransactionTypeEnum.WITHDRAWAL, 200.0, 1000000001.0)
        assert non_existent_transaction is None

    def test_create_transaction(self):
        repo = TransactionRepositoryMocky()
        
        new_transaction = Transaction(current_balance=500.0, timestamp=1000000001.0, value=500.0, type=TransactionTypeEnum.WITHDRAWAL)
        created_transaction = repo.create_transaction(new_transaction)
        
        assert created_transaction == new_transaction
        assert repo.get_transaction(TransactionTypeEnum.WITHDRAWAL, 500.0, 1000000001.0) == new_transaction

    def test_delete_transaction(self):
        repo = TransactionRepositoryMocky()
        
        deleted_transaction = repo.delete_transaction(TransactionTypeEnum.DEPOSIT, 1000000000.0, 1000000000.0)
        
        assert deleted_transaction.type == TransactionTypeEnum.DEPOSIT
        assert repo.get_transaction(TransactionTypeEnum.DEPOSIT, 1000000000.0, 1000000000.0) is None

        non_existent_transaction_deletion = repo.delete_transaction(TransactionTypeEnum.WITHDRAWAL, 200.0, 1000000001.0)
        assert non_existent_transaction_deletion is None

    def test_update_transaction(self):
        repo = TransactionRepositoryMocky()
        
        new_transaction_data = Transaction(current_balance=2000000000.0, timestamp=1000000000.0, value=1000000000.0, type=TransactionTypeEnum.DEPOSIT)
        updated_transaction = repo.update_transaction(TransactionTypeEnum.DEPOSIT, 1000000000.0, 1000000000.0, new_transaction_data)
        
        assert updated_transaction is not None
        assert updated_transaction.current_balance == 2000000000.0
        
        non_existent_transaction_update = repo.update_transaction(TransactionTypeEnum.WITHDRAWAL, 200.0, 1000000001.0, new_transaction_data)
        assert non_existent_transaction_update is None