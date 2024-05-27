from fastapi import FastAPI, HTTPException
from mangum import Mangum
from datetime import datetime

from ..app.entities.transaction import Transaction

from .environments import Environments

# from .repo.item_repository_mock import ItemRepositoryMock

# from .errors.entity_errors import ParamNotValidated

from .enums.transaction_type_enum import TransactionTypeEnum

# from .entities.item import Item


app = FastAPI()

user_repo = Environments.get_user_repo()()
transaction_repo = Environments.get_transaction_repo()

@app.get("/items/get_all_users")
def get_all_users():
    items = user_repo.get_all_users()

    users_list = list()
    for item in items:
        users_list.append(item.to_dict())
        
    return {
        "User": users_list
    }

@app.get("/")
def get_user():
    user = user_repo.get_user()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user.to_dict()

@app.post("/deposit")
def deposit(request: dict):
    user = user_repo.get_user()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    deposit_amount = sum(int(key) * int(value) for key, value in request.items())
    
    if deposit_amount == user.current_balance * 2:
        raise HTTPException(status_code=403, detail="Depósito suspeito")
    
    user.current_balance += deposit_amount
    
    timestamp = datetime.utcnow().timestamp() * 1000
    transaction = Transaction(type="deposit", value=deposit_amount, current_balance=user.current_balance, timestamp=timestamp)
    transaction_repo.create_transaction(transaction)
    
    return {
        "current_balance": user.current_balance,
        "timestamp": timestamp
    }

@app.post("/withdraw")
def withdraw(request: dict):
    user = user_repo.get_user()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    withdraw_amount = sum(int(key) * int(value) for key, value in request.items())
    
    if withdraw_amount > user.current_balance:
        raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")
    
    user.current_balance -= withdraw_amount
    
    timestamp = datetime.utcnow().timestamp() * 1000
    transaction = Transaction(type="withdraw", value=withdraw_amount, current_balance=user.current_balance, timestamp=timestamp)
    transaction_repo.create_transaction(transaction)
    
    return {
        "current_balance": user.current_balance,
        "timestamp": timestamp
    }

@app.get("/history")
def get_history():
    transactions = user_repo.get_user()
    if not transactions:
        raise HTTPException(status_code=400, detail="User not found")
    
    all_transactions = transaction_repo.get_all_transactions()
    
    transaction_history = []
    for transaction in all_transactions:
        transaction_history.append({
            "type": transaction.type,
            "value": transaction.value,
            "current_balance": transaction.current_balance,
            "timestamp": transaction.timestamp
        })
    
    return {"history": transaction_history}

# @app.get("/items/{item_id}")
# def get_item(item_id: int):
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     return {
#         "item_id": item_id,
#         "item": item.to_dict()    
#     }

# @app.post("/items/create_item", status_code=201)
# def create_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
#     if item is not None:
#         raise HTTPException(status_code=409, detail="Item already exists")
    
#     name = request.get("name")
#     price = request.get("price")
#     item_type = request.get("item_type")
#     if item_type is None:
#         raise HTTPException(status_code=400, detail="Item type is required")
#     if type(item_type) != str:
#         raise HTTPException(status_code=400, detail="Item type must be a string")
#     if item_type not in [possible_type.value for possible_type in ItemTypeEnum]:
#         raise HTTPException(status_code=400, detail="Item type is not a valid one")
    
#     admin_permission = request.get("admin_permission")
    
#     try:
#         item = Item(name=name, price=price, item_type=ItemTypeEnum[item_type], admin_permission=admin_permission)
#     except ParamNotValidated as err:
#         raise HTTPException(status_code=400, detail=err.message)
    
#     item_response = repo.create_item(item, item_id)
#     return {
#         "item_id": item_id,
#         "item": item_response.to_dict()    
#     }
    
# @app.delete("/items/delete_item")
# def delete_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     item_deleted = repo.delete_item(item_id)
    
#     return {
#         "item_id": item_id,
#         "item": item_deleted.to_dict()    
#     }
    
# @app.put("/items/update_item")
# def update_item(request: dict):
#     item_id = request.get("item_id")
    
#     validation_item_id = Item.validate_item_id(item_id=item_id)
#     if not validation_item_id[0]:
#         raise HTTPException(status_code=400, detail=validation_item_id[1])
    
#     item = repo.get_item(item_id)
    
#     if item is None:
#         raise HTTPException(status_code=404, detail="Item Not found")
    
#     if item.admin_permission == True:
#         raise HTTPException(status_code=403, detail="Item Not found")
    
#     name = request.get("name")
#     price = request.get("price")
#     admin_permission = request.get("admin_permission")
    
#     item_type_value = request.get("item_type")
#     if item_type_value != None:
#         if type(item_type_value) != str:
#             raise HTTPException(status_code=400, detail="Item type must be a string")
#         if item_type_value not in [possible_type.value for possible_type in ItemTypeEnum]:
#             raise HTTPException(status_code=400, detail="Item type is not a valid one")
#         item_type = ItemTypeEnum[item_type_value]
#     else:
#         item_type = None
        
#     item_updated = repo.update_item(item_id, name, price, item_type, admin_permission)
    
#     return {
#         "item_id": item_id,
#         "item": item_updated.to_dict()    
#     }
    


# handler = Mangum(app, lifespan="off")
