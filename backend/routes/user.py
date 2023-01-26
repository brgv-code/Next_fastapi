from fastapi import APIRouter, HTTPException, status
from models.user import users
from config.db import conn
from schemas.user import User
user = APIRouter()


@user.get("/")
async def get_user():
    return conn.execute(users.select()).fetchall()

# get user with id


@user.get("/{id}")
async def get_user(id: int):
    query = users.select().where(users.c.id == id)
    result = conn.execute(query).first()
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")
    return result
# post a user


@user.post("/")
async def create_user(user: User):
     conn.execute(users.insert().values(
        username=user.username, email=user.email, password=user.password))
     return  conn.execute(users.select()).fetchall()

# update user with id and user data
@user.put("/{id}")
async def update_user(id: int, user: User):
    query = users.update().where(users.c.id == id).values(
        username=user.username, email=user.email, password=user.password)
    conn.execute(query)
    return  conn.execute(users.select()).fetchall()

# delete user with id
@user.delete("/{id}")
async def delete_user(id: int):
    query = users.delete().where(users.c.id == id)
    conn.execute(query)
    return  conn.execute(users.select()).fetchall()