from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    name: str
    age: int

class UserResponse(BaseModel):
    id: int
    name: str
    age: int


@app.post("/create_user", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
    }


@app.get("/user", response_model=UserResponse)
def get_user():
    return {
        "id": 1,
        "name": "Adi",
        "age": 23
    }


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    return {
        "id": 1,
        "name": "Adi",
        "age": 23
    }