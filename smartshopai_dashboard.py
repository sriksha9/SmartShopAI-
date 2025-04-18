import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page setup
st.set_page_config(page_title="SmartShopAI Dashboard", layout="wide")
st.title(" SmartShopAI - Personalized E-Commerce Intelligence")
st.markdown("Forecast customer demand, recommend products, and tailor marketing — all in one dashboard.")

# Sidebar input
st.sidebar.header(" Select Customer")
selected_user = st.sidebar.text_input("Enter Customer ID", value="0")

# Load data files
@st.cache_data
def load_forecast():
    return pd.read_csv("forecast_per_customer_demo.csv")

@st.cache_data
def load_recommendations():
    return pd.read_csv("recs_multiuser_demo.csv")

forecast_df = load_forecast()
recs_df = load_recommendations()

# Validate input
try:
    customer_id = int(selected_user)
except ValueError:
    st.error("Please enter a valid numeric Customer ID")
    st.stop()

# PHASE 1: Forecast Graph
st.subheader("Forecasted Activity for Next 7 Days")
cust_forecast = forecast_df[forecast_df['customer_id'] == customer_id]

if cust_forecast.empty:
    st.warning("No forecast available for this customer.")
else:
    fig, ax = plt.subplots()
    ax.plot(cust_forecast['day'], cust_forecast['predicted_activity'], marker='o')
    ax.set_title(f"Predicted Activity for Customer {customer_id}")
    ax.set_ylabel("Predicted Activity")
    ax.set_xlabel("Day")
    ax.grid(True)
    st.pyplot(fig)

    # PHASE 3: Marketing Suggestion
    avg_activity = cust_forecast['predicted_activity'].mean()
    st.subheader(" Marketing Insight")
    if avg_activity >= 2:
        st.success(" High predicted engagement. Offer a loyalty reward or bundle deal.")
    elif 1 <= avg_activity < 2:
        st.info(" Moderate activity. Consider sending a product reminder or wishlist notification.")
    else:
        st.warning(" Low activity expected. Try offering a discount to re-engage this customer.")

# PHASE 2: Product Recommendations
st.subheader(" Recommended Products for Customer")
cust_recs = recs_df[recs_df['customer_id'] == customer_id]

if cust_recs.empty:
    st.warning("No product recommendations found for this customer.")
else:
    st.dataframe(
        cust_recs[['item_id', 'category_id', 'score']]
        .sort_values(by='score', ascending=False)
        .reset_index(drop=True)
    )

# Footer
st.markdown("---")
st.caption("SmartShopAI © 2025 | Built with LSTM, Streamlit & Customer Intelligence")
