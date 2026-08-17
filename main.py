from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Address(BaseModel):
    city: str
    state: str
    zip_code: str

class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address

# Home route
@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI application!"}

# About route
@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}

# User route
@app.get("/users")
def user():
    return {
        "user": ["Adi", "Mohit", "Rohit"]
    }

# User ID route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

# Query parameter route
@app.get("/search")
def search(name: str="Null"):
    return {"Name": name}

@app.get("/products")
def products(limit: int = 10):
    return {"limit": limit}

# Multiple query parameters route
@app.get("/items")
def items(name: str = "Null", price: int = 0):
    return {
        "name": name, 
        "price": price
        }


# Request Body + POST API + Pydantic
@app.post("/create-user")
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
        }


# Pydantic Models + Data Validation + Nested Schemas
@app.post("/create_user")
def create_user(user: User):
    return {
        "message": "User Created",
        "data": user
    }


# Nested Loops
@app.post("/create_user_with_address")
def create_user_with_address(user: User):
    return user