from sklearn.linear_model import LinearRegression
import pandas as pd

def predict_market_demand(data: pd.DataFrame):
    model = LinearRegression()
    X = data[["feature_usage", "search_volume"]]
    y = data["market_revenue"]
    model.fit(X, y)
    return model.predict(X[-1:].values)[0]
