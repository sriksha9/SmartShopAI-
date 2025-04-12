import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="SmartShopAI Dashboard", layout="wide")
st.title(" SmartShopAI - E-Commerce Intelligence Dashboard")
st.markdown("Enter a Customer ID to view personalized product recommendations and forecast.")

# Sidebar for Customer ID input
st.sidebar.header("Customer Selection")
customer_id = st.sidebar.text_input("Enter Customer ID", value="1532072415")

# --- Forecast Section ---
try:
    forecast_df = pd.read_csv("forecast.csv")
    forecast_days = len(forecast_df)
    days = [f"Day {i+1}" for i in range(forecast_days)]
    predicted_sales = forecast_df['Predicted_Sales'].values

    st.subheader(f" Predicted Sales (Next {forecast_days} Days)")
    fig, ax = plt.subplots()
    ax.plot(days, predicted_sales, marker='o')
    ax.set_xlabel("Future Days")
    ax.set_ylabel("Predicted Sales")
    ax.set_title("LSTM Sales Forecast")
    ax.grid(True)
    st.pyplot(fig)

except Exception as e:
    st.error(f" Error loading forecast.csv: {e}")

# --- Recommendation Section ---
try:
    recs_df = pd.read_csv("recs_multiuser.csv")
    recs_df['CustomerID'] = recs_df['CustomerID'].astype(str)

    st.subheader(" Personalized Product Recommendations")
    user_recs = recs_df[recs_df['CustomerID'] == customer_id]

    if not user_recs.empty:
        for _, row in user_recs.iterrows():
            st.markdown(f"- **Item ID:** {row['Item ID']} | **Category ID:** {row['Category ID']} | **Score:** {row['Score']}")
    else:
        st.warning("No recommendations found for this Customer ID.")

except Exception as e:
    st.error(f" Error loading recs_multiuser.csv: {e}")

# --- Marketing Insight Section ---
st.subheader(" Marketing Insight")
if 'user_recs' in locals() and not user_recs.empty:
    top_item = user_recs.sort_values("Score", ascending=False).iloc[0]
    st.success(f" Recommend offering a discount on Item {top_item['Item ID']} "
               f"(Category {top_item['Category ID']}) to increase conversions.")
else:
    st.info("Waiting for customer activity data to generate insights.")

# Footer
st.markdown("---")
st.caption("SmartShopAI - Streamlit Dashboard powered by LSTM + Behavior Intelligence")
