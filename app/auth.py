from jose import JWTError, jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

from app.config import ACCESS_TOKEN_EXPIRE, ALGO, SECRET_KEY


pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(data):
    to_encode= data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE)
    to_encode.update({"exp": expire})
    try:
        jwt_token =jwt.encode(to_encode, SECRET_KEY, algorithm=ALGO)
        return jwt_token
    except JWTError as jwterror:
        print(f"[Error] in jwt: {jwterror}")
    except Exception as e:
        print(f"[Error]: {e}")