from fastapi import FastAPI, HTTPException
from starlette import status
from schemas import CreateUserSchema, GetUserSchema, AppendOrdersSchema
from uuid import UUID
import requests
import random

app = FastAPI(debug=True)

USERS = []

@app.get('/users')
def get_users():
    return USERS

    # user_id_list = []
    # for user in USERS:
    #     user_id_list.append(user['user_id'])
    # return user_id_list

@app.get('/users/{user_id}', response_model=GetUserSchema)
def get_user(user_id: int):
    for user in USERS:
        if user['user_id'] == user_id:
            return user
    raise HTTPException(status_code=404, detail={'message': f"order {user_id} was not found"})

@app.post('/users', status_code=status.HTTP_201_CREATED, response_model=GetUserSchema)
def create_user(user: CreateUserSchema):
    new_user = user.model_dump()
    new_user['user_id'] = generate_user_id()
    new_user['orders'] = []
    USERS.append(new_user)
    return new_user

@app.put('/users/{user_id}/orders', response_model=GetUserSchema)
def add_order(user_id: int, orders: AppendOrdersSchema):
    for user in USERS:
        if user['user_id'] == user_id:
            user['orders'].append(order)
            return user
    raise HTTPException(status_code=404, detail={'message': f"order {user_id} was not found"})

def generate_user_id():
    user_id_exists = True
    while(user_id_exists):
        user_id = random.randint(0, 99999)

        user_id_exists = False
        for user in USERS:
            if user['user_id'] == user_id:
                user_id_exists = True
                break
            
        if not user_id_exists:
            return user_id