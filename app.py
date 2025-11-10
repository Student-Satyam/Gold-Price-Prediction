import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("📈 Gold Price Prediction App")
st.write("This app predicts the **next day's closing price** using a Random Forest Regressor.")

# Sidebar input
st.sidebar.header("Enter Market Data")

open_price = st.sidebar.number_input("Open Price", min_value=0.0)
high_price = st.sidebar.number_input("High Price", min_value=0.0)
low_price = st.sidebar.number_input("Low Price", min_value=0.0)
close_price = st.sidebar.number_input("Close Price", min_value=0.0)
volume = st.sidebar.number_input("Volume", min_value=0.0)
return_pct = st.sidebar.number_input("Return (%)", min_value=-10.0, max_value=10.0, value=0.0)
ma_5 = st.sidebar.number_input("MA 5", min_value=0.0)
ma_10 = st.sidebar.number_input("MA 10", min_value=0.0)
volatility_10 = st.sidebar.number_input("Volatility (10-day)", min_value=0.0)
lag1 = st.sidebar.number_input("Previous Close (Lag 1)", min_value=0.0)
lag2 = st.sidebar.number_input("Previous Close (Lag 2)", min_value=0.0)
lag3 = st.sidebar.number_input("Previous Close (Lag 3)", min_value=0.0)

# Create input DataFrame
input_data = pd.DataFrame({
    'Open': [open_price],
    'High': [high_price],
    'Low': [low_price],
    'Close': [close_price],
    'Volume': [volume],
    'Return': [return_pct / 100],
    'MA_5': [ma_5],
    'MA_10': [ma_10],
    'Volatility_10': [volatility_10],
    'Close_lag1': [lag1],
    'Close_lag2': [lag2],
    'Close_lag3': [lag3]
})

if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    st.success(f"📊 Predicted Next-Day Closing Price: **{prediction:.2f}**")
