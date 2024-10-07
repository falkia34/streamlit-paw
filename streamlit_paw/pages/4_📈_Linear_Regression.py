import streamlit as st
import joblib
import os
import numpy as np


def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model


st.set_page_config(
    page_title="Linear Regression - Streamlit App",
    page_icon="🔥",
)

st.title("Linear Regression")
st.subheader("Penentuan Gaji Karyawan Menggunakan Regresi Linier")

with st.form("my_form"):
    experience = st.slider("Berapa tahun pengalaman kerjanya?", 0, 20)

    submitted = st.form_submit_button("Proses")

if submitted:
    regressor = load_prediction_model("models/linear_regression_salary.pkl")
    experience_reshaped = np.array(experience).reshape(-1, 1)

    predicted_salary = regressor.predict(experience_reshaped)

    st.info("Gaji untuk karyawan dengan pengalaman bekerja {} tahun: {}".format(
        experience, (predicted_salary[0][0].round(2)))
    )
