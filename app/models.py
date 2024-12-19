from pydantic import BaseModel, Field
from datetime import date

class User(BaseModel):
    username: str
    password: str
    
class Expense(BaseModel):
    amount: float
    category: str
    description: str
    date: date
