import pandas as pd
from .data_sources import website_traffic, product_usage, social_media_sentiment, customer_feedback
from .models import demand_forecaster, feature_engagement_predictor

def run_market_demand_analysis():
    traffic_data = website_traffic.fetch_website_traffic('2025-01-01', '2025-10-31')
    usage_data = product_usage.get_usage_stats()
    sentiment_data = social_media_sentiment.analyze_social_media(["Example post"])
    feedback_data = customer_feedback.parse_feedback()

    combined_df = pd.concat([traffic_data, usage_data], axis=0)
    
    top_features = feature_engagement_predictor.identify_top_features(combined_df)
    demand_forecast = demand_forecaster.predict_market_demand(combined_df)

    insights = {
        "top_features": top_features,
        "predicted_demand": demand_forecast,
        "sentiment_summary": sentiment_data
    }

    return insights
