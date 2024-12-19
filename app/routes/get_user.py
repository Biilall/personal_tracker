from app.config import ALGO, SECRET_KEY
from fastapi import APIRouter, HTTPException, Depends
from app.db import user_collection
from fastapi.security import OAuth2PasswordBearer 
from jose import jwt, JWTError

oauth = OAuth2PasswordBearer(tokenUrl = "/auth/login")

def get_current_user(token = Depends(oauth)):
    try:
        payload = jwt.decode(token, SECRET_KEY , algorithms= [ALGO])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code = 401, detail="Invaild token")
        user = user_collection.find_one({"username": username})
        if user is None:
            raise HTTPException(status_code = 401, detail="user not found")
        
        return {"username": user["username"]} 
    except JWTError as je:
        raise HTTPException(status_code = 401, detail=f"{je}")