from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []


class Address(BaseModel):
    city: str
    state: str
    zip_code: str


class User(BaseModel):
    name: str
    age: int
    email: str
    address: Address


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


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
def get_users():
    return {
        "user": ["Adi", "Mohit", "Rohit"]
    }


# User ID route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}"
    }


# Query parameter route
@app.get("/search")
def search(name: str = "Null"):
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


# Create user with address
@app.post("/create_user_with_address")
def create_user_with_address(user: User):
    return user


# CRUD Operations for Todos ------------------

# Create Todos
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {
        "message": "Todo created successfully",
        "data": todo
    }

# Read Todos
@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    return {"message": "Todo not found"}

# Update Todos
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {
                "message": "Todo updated successfully",
                "data": updated_todo
            }
    return {"message": "Todo not found"}

# Delete Todos
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            deleted_todo = todos.pop(index)
            return {
                "message": "Todo deleted successfully",
                "data": deleted_todo
            }
    return {"message": "Todo not found"}