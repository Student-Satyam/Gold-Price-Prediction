# 📈 Stock Price Prediction (RandomForestRegressor + Streamlit)

This project predicts the **next day's stock closing price** using a **Random Forest Regressor** and displays it through a **Streamlit web app**.

---

## 🚀 Features
- Machine Learning model trained on historical stock data.
- Predicts next-day closing price.
- Interactive Streamlit UI.
- Ready for cloud deployment (Streamlit Cloud, Render, Hugging Face Spaces).

---

## 🧠 ML Model Details
- Model: **RandomForestRegressor**
- Data cleaning: removes duplicates, fills missing values.
- Features: Open, High, Low, Close, Volume, technical indicators, and lagged prices.
- **Train-Test Split**:  
  - Financial data is time-sensitive.  
  - We split data *chronologically* (first 80% for training, last 20% for testing).  
  - This ensures future prices don’t leak into past data (avoiding overfitting).
