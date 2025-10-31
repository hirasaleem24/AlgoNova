"""
Algonova Market Demand Analyzer
-------------------------------
This package provides the AI-Powered Market Demand Analyzer — a machine learning
feature that evaluates customer interactions, search trends, and feedback data
to forecast which product features are likely to gain the most market traction.

Modules:
    analyzer: Main entry point that runs the full market demand analysis pipeline.
    data_sources: Fetches and processes data from website traffic, usage stats, sentiment, etc.
    models: Machine learning models for demand forecasting and feature engagement.
    utils: Helper functions for data cleaning, transformation, and report generation.

Example usage:
    from algonova.market_demand_analyzer import run_market_demand_analysis

    insights = run_market_demand_analysis()
    print(insights)

Author: Algonova Product Intelligence Team
Version: 1.0.0
"""

from .analyzer import run_market_demand_analysis
from .models.demand_forecaster import predict_market_demand
from .models.feature_engagement_predictor import identify_top_features

__all__ = [
    "run_market_demand_analysis",
    "predict_market_demand",
    "identify_top_features",
]

__version__ = "1.0.0"
