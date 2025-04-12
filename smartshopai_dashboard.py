
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="SmartShopAI Dashboard", layout="wide")
st.title("🛍 SmartShopAI - E-Commerce Intelligence Dashboard")
st.markdown("Forecast future demand and recommend products using LSTM and behavioral interaction scoring.")

# Load forecast.csv
try:
    forecast_df = pd.read_csv("forecast.csv")
    forecast_days = len(forecast_df)
    days = [f"Day {i+1}" for i in range(forecast_days)]
    predicted_sales = forecast_df['Predicted_Sales'].values

    st.subheader(f"📈 Predicted Sales (Next {forecast_days} Days)")
    fig, ax = plt.subplots()
    ax.plot(days, predicted_sales, marker='o')
    ax.set_xlabel("Future Days")
    ax.set_ylabel("Predicted Sales")
    ax.set_title("LSTM Sales Forecast")
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"⚠️ Error loading forecast.csv: {e}")

# Load recs.csv
try:
    recs_df = pd.read_csv("recs.csv")

    st.subheader("🎯 Top Recommended Products (Based on Behavior Score)")
    if not recs_df.empty:
        for _, row in recs_df.iterrows():
            st.markdown(f"- **Item ID:** {row['Item ID']} | **Category ID:** {row['Category ID']} | **Score:** {row['Score']}")
    else:
        st.warning("No recommendations available in recs.csv.")

except Exception as e:
    st.error(f"⚠️ Error loading recs.csv: {e}")

# Marketing insight
st.subheader("💡 Marketing Insight")
try:
    if not recs_df.empty:
        top_item = recs_df.sort_values("Score", ascending=False).iloc[0]
        st.success(f"✅ Recommend sending a discount campaign for Item {top_item['Item ID']} (Category {top_item['Category ID']}) to boost conversions.")
    else:
        st.info("No marketing insight available yet.")
except:
    st.info("Marketing insights unavailable.")

# Footer
st.markdown("---")
st.caption("SmartShopAI - Streamlit Dashboard powered by LSTM + Behavior Intelligence")
