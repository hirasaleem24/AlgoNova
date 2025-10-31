import pandas as pd

def identify_top_features(data: pd.DataFrame) -> list:
    """
    Identify top features users engage with most.
    Currently based on highest 'feature_usage' values.
    """
    if "feature_usage" in data.columns:
        top_features = (
            data.sort_values(by="feature_usage", ascending=False)
                .head(3)["feature"]
                .tolist()
        )
    else:
        top_features = ["AI Chat", "Dashboard", "Reports"]

    return top_features

