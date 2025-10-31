"""
visualizer.py
-------------
Provides visualization utilities for the AI-Powered Market Demand Analyzer.

Uses Plotly to display:
- Top requested or most engaged features
- Sentiment analysis summary
- Predicted market demand level

Example:
    from algonova.market_demand_analyzer import analyzer, visualizer

    insights = analyzer.run_market_demand_analysis()
    visualizer.show_analysis_dashboard(insights)
"""

import plotly.graph_objects as go
from plotly.subplots import make_subplots


def show_analysis_dashboard(insights: dict):
    """
    Display a dashboard of market demand analysis results using Plotly.

    Args:
        insights (dict): Output dictionary from run_market_demand_analysis()
    """
    top_features = insights.get("top_features", [])
    sentiment = insights.get("sentiment_summary", {})
    demand_score = insights.get("predicted_market_demand", 0)
    feedback = insights.get("feedback_highlights", [])

    # --- 1️⃣ Bar Chart for Top Features ---
    feature_fig = go.Bar(
        x=top_features,
        y=[i * 100 for i in range(len(top_features), 0, -1)],
        marker_color="cornflowerblue",
        name="Top Features"
    )

    # --- 2️⃣ Pie Chart for Sentiment Summary ---
    sentiment_fig = go.Pie(
        labels=list(sentiment.keys()),
        values=list(sentiment.values()),
        hole=0.4,
        name="Sentiment",
        marker=dict(colors=["seagreen", "gold", "indianred"])
    )

    # --- 3️⃣ Gauge Chart for Demand Forecast ---
    gauge_fig = go.Indicator(
        mode="gauge+number",
        value=demand_score * 100,
        title={"text": "Predicted Market Demand (%)"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "dodgerblue"},
            "steps": [
                {"range": [0, 50], "color": "lightcoral"},
                {"range": [50, 80], "color": "khaki"},
                {"range": [80, 100], "color": "lightgreen"}
            ]
        },
        domain={"row": 0, "column": 1}
    )

    # --- Combine into a single dashboard layout ---
    fig = make_subplots(
        rows=2, cols=2,
        specs=[[{"type": "xy"}, {"type": "indicator"}],
               [{"type": "domain", "colspan": 2}, None]],
        subplot_titles=("Top Engaged Features", "Demand Forecast", "Sentiment Breakdown")
    )

    fig.add_trace(feature_fig, row=1, col=1)
    fig.add_trace(gauge_fig, row=1, col=2)
    fig.add_trace(sentiment_fig, row=2, col=1)

    fig.update_layout(
        title_text="📊 Algonova AI-Powered Market Demand Insights Dashboard",
        height=800,
        showlegend=False
    )

    fig.show()

    # --- Print feedback highlights below chart ---
    print("\n💬 Customer Feedback Highlights:")
    for comment in feedback:
        print(f" - {comment}")
