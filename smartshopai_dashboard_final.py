
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="SmartShopAI Dashboard", layout="wide")
st.title("🛍 SmartShopAI - E-Commerce Intelligence Dashboard")
st.markdown("Forecast future demand and recommend products using LSTM and user behavior.")

# Sidebar
st.sidebar.header("🔎 Select Options")
selected_user = st.sidebar.text_input("Enter Customer ID", value="1532072415")

# Load real forecast data
try:
    forecast_df = pd.read_csv("forecast.csv")
    forecast_days = len(forecast_df)
    dates = [f"Day {i+1}" for i in range(forecast_days)]
    predicted_sales = forecast_df['Predicted_Sales'].values

    st.subheader(f"📈 Real Predicted Sales (Next {forecast_days} Days)")
    fig, ax = plt.subplots()
    ax.plot(dates, predicted_sales, marker='o')
    ax.set_xlabel("Date")
    ax.set_ylabel("Predicted Sales")
    ax.set_title("Sales Forecast (LSTM)")
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Error loading forecast.csv: {e}")

# Load recommendations
try:
    recs_df = pd.read_csv("recs.csv")

    st.subheader(f"🎯 Recommended Products for Customer: {selected_user}")
    if not recs_df.empty:
        for _, row in recs_df.iterrows():
            st.markdown(f"- **Item ID:** {row['Item ID']} | **Category:** {row['Category ID']} | **Score:** {row['Score']}")
    else:
        st.warning("No recommendations found for this user.")

except Exception as e:
    st.error(f"Error loading recs.csv: {e}")

# Marketing insight
st.subheader("💡 Marketing Insight")
try:
    if not recs_df.empty:
        top_item = recs_df.sort_values("Score", ascending=False).iloc[0]
        st.success(f"Suggest offering a 10% discount for Item {top_item['Item ID']} (Category {top_item['Category ID']}) to drive conversions.")
    else:
        st.info("Waiting on user engagement data for marketing suggestions.")
except:
    st.info("No marketing insight available.")

# Footer
st.markdown("---")
st.caption("SmartShopAI - Powered by LSTM & Streamlit")
