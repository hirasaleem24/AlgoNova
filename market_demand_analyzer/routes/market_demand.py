from fastapi import APIRouter
from algonova.market_demand_analyzer.analyzer import run_market_demand_analysis

router = APIRouter()

@router.get("/market-demand/insights")
def get_market_demand_insights():
    results = run_market_demand_analysis()
    return results
