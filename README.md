
# 🛍️ SmartShopAI – E-Commerce Intelligence Dashboard

SmartShopAI is an intelligent, AI-powered dashboard designed to support e-commerce businesses by:

- 📈 Forecasting future product demand using LSTM-based time series models  
- 🎯 Generating personalized product recommendations using customer behavior  
- 💡 Providing actionable marketing insights to improve engagement and retention

This project combines deep learning with user behavior analytics to enable data-driven decision-making in modern online retail.

---

## ✅ Features

- 🔮 **LSTM Sales Forecasting** – Predicts future daily demand (next 14 days) based on historical transactions  
- 🧠 **Behavioral Recommendations** – Suggests top items using weighted user actions:  
  ‣ view = 1 | add-to-cart = 2 | transaction = 3  
- 📊 **Marketing Insights** – Recommends which product to promote (e.g., “10% off top scoring item”)

---

## 📁 Project Structure

```
SmartShopAI/
├── smartshopai_dashboard_updated.py     # Streamlit dashboard app
├── forecast.csv                         # 14-day LSTM forecast output
├── recs.csv                             # Personalized product recommendations
├── requirements.txt                     # Python dependencies
├── README.md                            # Project overview (this file)
└── notebooks/
    └── SmartShopAI_Modeling.ipynb       # ML modeling pipeline
```

---

## 📊 Dataset

The project uses a real-world e-commerce dataset containing:
- User behavior logs: views, add-to-carts, purchases
- Item metadata: category IDs
- Timestamps for time-series forecasting

---

## 🚀 How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/yourusername/SmartShopAI.git
cd SmartShopAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the dashboard:
```bash
streamlit run smartshopai_dashboard_updated.py
```

---

## 🌐 Deployment (Optional)

You can deploy this app using [Streamlit Cloud](https://streamlit.io/cloud) by linking your GitHub repository.

---

## 📌 Key Technologies

- Python
- Streamlit
- TensorFlow / Keras (LSTM)
- Pandas, NumPy, Matplotlib

---

## 📬 Contact

Created by **[Your Name]**  
For academic and demonstration purposes.  
LinkedIn: [your-link] | GitHub: [yourusername]
