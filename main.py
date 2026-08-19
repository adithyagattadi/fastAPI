from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class user_not_found_exception(Exception):
    def __init__(self, name:str):
        self.name = name

@app.exception_handler(user_not_found_exception)
def user_not_found_handler(request: Request, exc: user_not_found_exception):
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": f"User {exc.name} not found"
        }
    )

@app.get("/user/{name}")
def get_user(name:str):
    if name != "Adi":
        raise user_not_found_exception(
            name
        )
    return{
        "name":name
    }

# @app.get("/users/{user_id}")
# def get_user(user_id:int):
#     if user_id != 1:
#         raise HTTPException(
#             status_code = 404,
#             detail = "User not found"
#         )
#     return{
#         "id": 1,
#         "name": "Adi"
#     }