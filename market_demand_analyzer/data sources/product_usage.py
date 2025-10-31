import pandas as pd

def get_usage_stats(start_date: str, end_date: str) -> pd.DataFrame:
    """Simulate product usage statistics."""
    data = {
        "feature": ["AI Chat", "Dashboard", "API Integration", "Reports"],
        "feature_usage": [0.9, 0.7, 0.8, 0.5],
        "market_revenue": [50000, 42000, 48000, 30000]
    }
    return pd.DataFrame(data)

