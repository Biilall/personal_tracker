from app.routes.get_user import get_current_user
from fastapi import APIRouter, HTTPException, Depends
from app.db import expense_collection
from app.models import Expense


router = APIRouter()


@router.post("/expenses")
def create_expenses(expense: Expense, user = Depends(get_current_user)):
    expense_data = expense.dict()
    
    expense_data["user"] = user
    result = expense_collection.insert_one(expense_data)
    print("result.inserted_id", result.inserted_id)
    return {"_id": str(result.inserted_id), **expense_data}


@router.get("/expenses")
def list_expenses(start_date = None, end_date = None, user = Depends(get_current_user)):
    query = {"user": user}
    
    if start_date and end_date:
        query['date'] = {"$gte": start_date, "$lte": end_date}
    
    return list(expense_collection.find(query))
