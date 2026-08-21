from fastapi import FastAPI, Depends, Header, HTTPException

app = FastAPI()

def verify_token(token: str = Header(None)):
    if token != "my_secret_token":
        raise HTTPException(
            status_code=404,
            detail= "Unauthorized"
        )
    return{
        "user": "Authorized User"
    }

@app.get("/secure-data")
def secure_data(user=Depends(verify_token)):
    return{
        "message": "secure data access",
        "user":user 
    }

# def common_logic():
#     return{
#         "message": "common logic executed"
#     }
# @app.get("/home")
# def home(data=Depends(common_logic)):
#     return data

# def get_current_user():
#     return {
#         "user": "mohit"
#     }

# @app.get("/profile")
# def profile(user=Depends(get_current_user)):
#     return user

# @app.get("/dashboard")
# def profile(user=Depends(get_current_user)):
#     return user


