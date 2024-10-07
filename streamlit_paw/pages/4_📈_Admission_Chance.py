import streamlit as st
import joblib
import os


def load_prediction_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    return loaded_model


st.set_page_config(
    page_title="Admission Chance - Streamlit App",
    page_icon="🔥",
)

st.title("Admission Chance")
st.subheader("Prediksi Potensi Diterima Program Graduate dengan Regresi Linier")

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
    regressor = load_prediction_model(
        "models/linear_regression_grad_admission.pkl"
    )

    predicted_result = regressor.predict(
        [[gre, toefl, univ_rating, sop, lor, cgpa, research_exp]])

    st.info("Chance of getting admission: {}%".format(
        (predicted_result[0]*100).round(2))
    )
