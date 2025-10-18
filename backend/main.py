from fastapi import FastAPI
from comparison import display_comparison
from transaction_flow import simulate_transaction

app = FastAPI(title="AlgoNova API")

@app.get("/")
def home():
    return {"message": "Welcome to AlgoNova API"}

@app.get("/compare")
