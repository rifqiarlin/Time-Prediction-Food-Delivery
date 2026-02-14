import streamlit as st
import pandas as pd
from joblib import load

# =========================
# Load trained Lasso model
# =========================
model = load("best_lasso_model.pkl")  # pastikan file ini ada di folder yang sama

st.set_page_config(page_title="Delivery Time Prediction", layout="centered")

st.title("🕒 Food Delivery Time Prediction")
st.write("Input Data to Predict the **Delivery Time (minutes)**.")

# =========================
# Input Features
# =========================
st.subheader("Input Data Delivery")

Distance_km = st.slider("Distance (km)", min_value=0.0, value=20.0)
Weather = st.selectbox("Weather", ["Clear", "Windy", "Foggy", "Rainy"])
Traffic_Level = st.selectbox("Traffic Level", ["Low", "Medium", "High"])
Time_of_Day = st.selectbox("Time of Day", ["Morning", "Afternoon", "Evening", "Night"])
Vehicle_Type = st.selectbox("Vehicle Type", ["Bike", "Scooter", "Car"])
Preparation_Time_min = st.slider("Preparation Time (minutes)", min_value=1, max_value=60, value=15)
Courier_Experience_yrs = st.slider("Courier Experience (years)", min_value=0.0, max_value=20.0, value=2.0, step=0.5)

# =========================
# Predict Button
# =========================
if st.button("Predict Delivery Time"):

    # Buat dataframe sesuai format training (tanpa Order_ID & target)
    input_df = pd.DataFrame({
        "Distance_km": [Distance_km],
        "Weather": [Weather],
        "Traffic_Level": [Traffic_Level],
        "Time_of_Day": [Time_of_Day],
        "Vehicle_Type": [Vehicle_Type],
        "Preparation_Time_min": [Preparation_Time_min],
        "Courier_Experience_yrs": [Courier_Experience_yrs],
    })

    # Prediksi
    prediction = model.predict(input_df)[0]

    # Tampilkan hasil
    st.subheader("Prediction Result")
    st.success(f"Estimated delivery time: {prediction:,.1f} minutes")


# =========================
# Footer
# =========================
st.markdown("---")
st.caption("Model: Best Lasso Regression (GridSearchCV) | Target: Delivery_Time_min")