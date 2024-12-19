from app.routes.get_user import get_current_user
from fastapi import APIRouter, HTTPException, Depends
from app.auth import hash_password, verify_password, create_access_token
from app.db import user_collection
from app.models import User

router = APIRouter()
            
            
@router.post("/register")
def register(user: User):
    if user_collection.find_one({"username": user.username}):
        raise HTTPException(status_code = 400, detail="User already exists")
    
    user.password = hash_password(user.password)
    user_collection.insert_one(user.dict())
    return {"message": "User has been registered successfully"}


@router.post("/login")
def login(user: User):
    db_user = user_collection.find_one({"username": user.username})
    
    if not db_user or not verify_password(user.password, db_user['password']):
        raise HTTPException(status_code = 401, detail="Invaild creds")
    
    token = create_access_token({"sub": user.username})
    return {"access_token": token, "token_type": "Bearer"}

@router.post("/profile")
def profile(token = Depends(get_current_user)):
    return {"username": token}