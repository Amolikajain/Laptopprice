import streamlit as st
import pickle
import pandas as pd

# Load pipeline
pipeline = pickle.load(open('pipeline.pkl', 'rb'))

st.title("💻 Laptop Price Predictor")

# Inputs
company = st.selectbox("Company", ["Dell", "HP", "Lenovo", "Asus", "Apple"])
typename = st.selectbox("Type", ["Notebook", "Gaming", "Ultrabook"])
ram = st.slider("RAM (GB)", 2, 64, 8)
weight = st.slider("Weight (kg)", 1.0, 5.0, 2.0)
inches = st.slider("Screen Size", 10.0, 20.0, 15.6)

cpu = st.text_input("CPU (e.g., Intel Core i5)")
gpu = st.text_input("GPU (e.g., Nvidia GTX 1650)")
memory = st.text_input("Storage (e.g., 512GB SSD)")
opsys = st.selectbox("OS", ["Windows", "MacOS", "Linux"])

if st.button("Predict Price"):

    input_df = pd.DataFrame({
        'Company': [company],
        'TypeName': [typename],
        'Inches': [inches],
        'Ram': [ram],
        'Weight': [weight],
        'Cpu': [cpu],
        'Gpu': [gpu],
        'OpSys': [opsys],
        'Memory': [memory]
    })

    prediction = pipeline.predict(input_df)

    st.success(f"Estimated Price: €{round(prediction[0], 2)}")