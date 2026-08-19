from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

{
    "name": "Adi",
    "age": 23,
    "Password": 12345
}

class User(BaseModel):
    name:str
    age:int
    password:str

class userResponse(BaseModel):
    name:str
    age:int

@app.get("/user", response_model=userResponse)
def get_user():
    return{
        "name":"Adi",
        "age":23,
        "password":12345
    }