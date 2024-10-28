import streamlit as st
import joblib
import os
import numpy as np
from streamlit_navigation_bar import st_navbar


st.set_page_config(
    page_title="Linear Regression - Streamlit App",
    page_icon="🔥",
    initial_sidebar_state="collapsed",
)

styles = {
    "nav": {
        "background-color": "royalblue",
    },
    "img": {
        "padding-right": "14px",
    },
    "span": {
        "color": "white",
        "border-radius": "0.5rem",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(255, 255, 255, 0.25)",
    },
    "hover": {
        "background-color": "rgba(255, 255, 255, 0.35)",
    },
}

page = st_navbar(["Home", "Statistics", "Calculation", "Sentiment Analysis",
                 "Regression", "Image Classification", "About"], selected="Regression", styles=styles)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
if page == "Calculation":
    st.switch_page("pages/2_🔢_Calculation.py")
if page == "Sentiment Analysis":
    st.switch_page("pages/3_😶_Sentiment_Analysis.py")
if page == "Image Classification":
    st.switch_page("pages/5_👻_Bisindo_Gesture.py")
if page == "About":
    st.switch_page("pages/6_🔣_About.py")


@st.cache_resource
def load_model(model_file):
    loaded_model = joblib.load(
        open(os.path.join('streamlit_paw/models', model_file), "rb"))
    return loaded_model


st.title("Linear Regression")
st.subheader("Penentuan Gaji Karyawan Menggunakan Regresi Linier")

menu = ["Salary Prediction", "Admission Chance"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Admission Chance":
    st.switch_page("pages/4_📈_Admission_Chance.py")

regressor = load_model("linear_regression_salary.pkl")

with st.form("my_form"):
    experience = st.slider("Berapa tahun pengalaman kerjanya?", 0, 20)

    submitted = st.form_submit_button("Proses")

if submitted:
    experience_reshaped = np.array(experience).reshape(-1, 1)

    predicted_salary = regressor.predict(experience_reshaped)

    st.info("Gaji untuk karyawan dengan pengalaman bekerja {} tahun: {}".format(
        experience, (predicted_salary[0][0].round(2)))
    )
