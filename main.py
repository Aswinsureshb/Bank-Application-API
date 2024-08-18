from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    id: int
    date: str
    account: int
    amount: float
    type: str
    
transactions = [
        Transaction(id = 1, date = "2024-02-14",account = 1, amount = 250.00, type= "Credit"),
        Transaction(id = 2, date = "2024-02-15",account = 2, amount = 100.00, type= "Debit"),
        Transaction(id = 3, date = "2024-02-16",account = 1, amount = 230.00, type= "Credit"),
        Transaction(id = 4, date = "2024-02-17",account = 2, amount = 520.00, type= "Debit"),
        Transaction(id = 5, date = "2024-02-18",account = 1, amount = 200.00, type= "Credit"),
        Transaction(id = 6, date = "2024-02-19",account = 2, amount = 23.00, type= "Credit"),
        Transaction(id = 7, date = "2024-02-20",account = 1, amount = 289.00, type= "Debit"),
        Transaction(id = 8, date = "2024-02-21",account = 1, amount = 252.00, type= "Credit")
        
]
    
@app.get("/transaction", response_model = List[Transaction])
def return_transaction():
        return transactions
    


totalbalance = 1000.00


@app.get("/totalbalance")
def get_balance():
    return {totalbalance}


@app.get("/deposit/{input1}")
def deposit_to_account(input1: float):
    global totalbalance
   
    return {input1+totalbalance}

@app.get("/withdraw/{input2}")
def withdraw_from_account(input2: float):
    global totalbalance
    if input2 > totalbalance:
        return {"error": "Insufficient funds"}
    totalbalance -= input2
    return {totalbalance}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
