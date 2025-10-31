
import pandas as pd

def fetch_website_traffic(start_date: str, end_date: str) -> pd.DataFrame:
    """Simulate website traffic data."""
    data = {
        "feature": ["AI Chat", "Dashboard", "API Integration", "Reports"],
        "visits": [2500, 1800, 2200, 1500],
        "search_volume": [400, 300, 350, 200]
    }
    return pd.DataFrame(data)
