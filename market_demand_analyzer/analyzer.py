
"""
analyzer.py
-----------
Core logic for the AI-Powered Market Demand Analyzer.

This module orchestrates data gathering, processing, and model-based
predictions to generate insights on product demand trends and
feature engagement.

Example:
    from algonova.market_demand_analyzer import run_market_demand_analysis

    insights = run_market_demand_analysis()
    print(insights)
"""

import pandas as pd
from datetime import datetime

# Import data sources (you can replace these stubs with actual integrations)
from .data_sources import website_traffic, product_usage, social_media_sentiment, customer_feedback
from .models import demand_forecaster, feature_engagement_predictor


def run_market_demand_analysis(start_date: str = "2025-01-01", end_date: str = None) -> dict:
    """
    Runs the full market demand analysis pipeline.

    Args:
        start_date (str): The start date for the data range (YYYY-MM-DD).
        end_date (str): The end date for the data range. Defaults to today.

    Returns:
        dict: Insights containing top features, predicted market demand, and sentiment overview.
    """
    if end_date is None:
        end_date = datetime.today().strftime("%Y-%m-%d")

    print(f"Running Market Demand Analysis from {start_date} to {end_date}...")

    # Step 1: Fetch Data from All Sources
    traffic_data = website_traffic.fetch_website_traffic(start_date, end_date)
    usage_data = product_usage.get_usage_stats(start_date, end_date)
    sentiment_data = social_media_sentiment.analyze_social_media()
    feedback_data = customer_feedback.parse_feedback()

    # Step 2: Combine the data into a single dataset
    print("Combining datasets...")
    combined_df = pd.concat([traffic_data, usage_data], axis=0, ignore_index=True)

    # Step 3: Generate Insights
    print("Identifying top features...")
    top_features = feature_engagement_predictor.identify_top_features(combined_df)

    print("Predicting market demand...")
    predicted_demand = demand_forecaster.predict_market_demand(combined_df)

    print("Summarizing sentiment...")
    sentiment_summary = sentiment_data  # already processed as a dict

    # Step 4: Build the insights dictionary
    insights = {
        "report_generated_at": datetime.now().isoformat(),
        "top_features": top_features,
        "predicted_market_demand": predicted_demand,
        "sentiment_summary": sentiment_summary,
        "feedback_highlights": feedback_data,
    }

    print("Market Demand Analysis complete ✅")
    return insights


# Optional: Quick test run when executed directly
if __name__ == "__main__":
    results = run_market_demand_analysis()
    print("\n=== Market Demand Insights ===")
    for key, value in results.items():
        print(f"{key}: {value}")
