

import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
import streamlit as st
import os

# Streamlit configuration
st.set_page_config(page_title="Liver Cirrhosis Stage Detection", layout='centered', page_icon="🎉")

# Custom UI styling
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: white;
    }
    .css-1d391kg, .css-1v3fvcr {
        background-color: #1c1e26;
        border: 1px solid #333;
        padding: 1em;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🧬 Liver Cirrhosis Stage Predictor")
st.write("Provide the following clinical parameters to predict the cirrhosis stage.")

model = joblib.load("model_s.pkl")
scaler = joblib.load("scl.pkl")

# Input form

N_Days = st.number_input("N_days", min_value=0, max_value=8000, value=2000)
# age_y = st.number_input("Age", min_value=0, max_value=100, value=51)
Status = st.selectbox("Status", ['C', 'CL', 'D'])
Drug = st.selectbox("Drug", ['D-penicillamine', 'Placebo'])
Sex = st.selectbox("Sex", ['Male', 'Female'])
Ascites = st.selectbox("Ascites", ['Yes', 'No'])
Hepatomegaly = st.selectbox("Hepatomegaly", ['Yes', 'No'])
Spiders = st.selectbox("Spiders", ['Yes', 'No'])
Edema = st.selectbox("Edema", ['N', 'S', 'Y'])
Bilirubin = st.number_input("Bilirubin", min_value=0.0, max_value=30.0, step=0.1)
Cholesterol = st.number_input("Cholesterol", min_value=0, max_value=800)
Albumin = st.number_input("Albumin", min_value=0.0, max_value=20.0, step=0.1)
Copper = st.number_input("Copper", min_value=0, max_value=400)
Alk_Phos = st.number_input("Alk_Phos", min_value=0, max_value=1000)
SGOT = st.number_input("SGOT", min_value=0, max_value=1000)
Tryglicerides = st.number_input("Tryglicerides", min_value=0, max_value=1000)
Platelets = st.number_input("Platelets", min_value=0, max_value=1000)
Prothrombin = st.number_input("Prothrombin", min_value=0.0, max_value=900.0, step=0.1)
age_y = st.number_input("Age", min_value=0, max_value=100, value=51)

edema_map = {'N': 0, 'S': 1, 'Y': 2}
status_map = {'C': 0, 'CL': 1, 'D': 2}

if st.button("Predict Cirrhosis Stage"):
    input_dict = {
            'N_Days': N_Days,
            'age_y': age_y,
            'Status': status_map[Status],
            'Drug': 1 if Drug == "D-penicillamine" else 0,
            'Sex': 1 if Sex == "Female" else 0,
            'Ascites': 1 if Ascites == "Yes" else 0,
            'Hepatomegaly': 1 if Hepatomegaly == "Yes" else 0,
            'Spiders': 1 if Spiders == "Yes" else 0,
            'Edema': edema_map.get(Edema, 0),
            'Bilirubin': Bilirubin,
            'Cholesterol': Cholesterol,
            'Albumin': Albumin,
            'Copper': Copper,
            'Alk_Phos': Alk_Phos,
            'SGOT': SGOT,
            'Tryglicerides': Tryglicerides,
            'Platelets': Platelets,
            'Prothrombin': Prothrombin,
            'age_y': age_y,
        }
    

    column_order = ['N_Days', 'Status', 'Drug', 'Sex', 'Ascites', 'Hepatomegaly',
                    'Spiders', 'Edema', 'Bilirubin', 'Cholesterol', 'Albumin', 'Copper',
                    'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'age_y']
    inp_df = pd.DataFrame([input_dict])[column_order]
    
    
    s_col = ['N_Days','Cholesterol', 'Albumin', 'Copper', 'Alk_Phos', 'SGOT', 'Tryglicerides', 'Platelets', 'Prothrombin', 'age_y']
    inp_df[s_col] = scaler.transform(inp_df[s_col])


    prediction = model.predict(inp_df)[0]
    proba = model.predict_proba(inp_df)[0]
    ppd = np.argmax(proba)
    
    st.success(f"Predicted Stage: Stage {prediction}")
    st.subheader("Prediction Confidence:")
    for i, p in enumerate(proba):
        st.write(f"Stage {i+1}: {p*100:.2f}% confidence")
            
            

