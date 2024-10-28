import streamlit as st
import joblib
import os
from streamlit_navigation_bar import st_navbar


st.set_page_config(
    page_title="Admission Chance - Streamlit App",
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


st.title("Admission Chance")
st.subheader("Prediksi Potensi Diterima Program Graduate dengan Regresi Linier")

menu = ["Salary Prediction", "Admission Chance"]
choice = st.sidebar.selectbox("Menu", menu, index=1)

if choice == "Salary Prediction":
    st.switch_page("pages/4_📈_Linear_Regression.py")

regressor = load_model("linear_regression_grad_admission.pkl")

with st.form("my_form"):
    gre = st.slider("GRE Score", 260, 340, 290)
    toefl = st.slider("TOEFL Score", 0, 120, 85)
    univ_rating = st.slider("University Rating", 0, 5, 3)
    sop = st.slider("Statement of Purpose Strength", 0, 5, 3)
    lor = st.slider("Letter of Recommendation Strength", 0, 5, 3)
    cgpa = st.slider("Undergraduate GPA", 0, 10, 6)
    research_exp = st.checkbox("Has research Experience", [0, 1])

    submitted = st.form_submit_button("Process")

if submitted:
    predicted_result = regressor.predict(
        [[gre, toefl, univ_rating, sop, lor, cgpa, research_exp]])

    st.info("Chance of getting admission: {}%".format(
        (predicted_result[0]*100).round(2))
    )
