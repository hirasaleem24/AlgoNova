import streamlit as st
from algonova.market_demand_analyzer import analyzer, visualizer

st.set_page_config(page_title="Algonova AI Market Demand Analyzer", layout="wide")

st.title("🤖 Algonova Market Demand Analyzer")
st.markdown("Gain AI-powered insights into customer demand, engagement, and sentiment.")

# Run analysis
if st.button("Run Market Analysis"):
    with st.spinner("Running AI analysis..."):
        insights = analyzer.run_market_demand_analysis()
        st.success("Analysis complete!")

        st.subheader("📊 Insights Summary")
        st.json(insights)

        st.subheader("📈 Interactive Dashboard")
        visualizer.show_analysis_dashboard(insights)
