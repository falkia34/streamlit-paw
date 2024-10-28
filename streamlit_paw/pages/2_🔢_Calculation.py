import streamlit as st
import time
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="Calculation - Streamlit App",
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
options = {
    "show_sidebar": False,
}

page = st_navbar(["Home", "Statistics", "Calculation", "Sentiment Analysis",
                 "Regression", "Image Classification", "About"], selected="Calculation", styles=styles, options=options)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
if page == "Sentiment Analysis":
    st.switch_page("pages/3_😶_Sentiment_Analysis.py")
if page == "Regression":
    st.switch_page("pages/4_📈_Linear_Regression.py")
if page == "Image Classification":
    st.switch_page("pages/5_👻_Bisindo_Gesture.py")
if page == "About":
    st.switch_page("pages/6_🔣_About.py")

st.title(":1234: Calculation")

# Initialize session state if not already done
if 'counter' not in st.session_state:
    st.session_state.counter = 0

# Function to increment counter


def increment_counter():
    st.session_state.counter += 1

# Function to simulate a time-consuming operation with caching


@st.cache_data
def expensive_computation(x):
    time.sleep(2)  # Simulate a long computation
    return x ** 2


# Spinner to show during the loading of the computation
with st.spinner('Calculating...'):
    # Cached computation
    result = expensive_computation(st.session_state.counter)

# Display the result
st.success(f"Result of the computation: {result}")

# Button to increment counter with callback
if st.button("Increment Counter", on_click=increment_counter):
    st.write("Counter incremented!")

# Display the current counter value
st.info(f"Current counter value: {st.session_state.counter}")

# Example of using session state with callback


def reset_counter():
    st.session_state.counter = 0


# Button to reset counter with callback
st.button("Reset Counter", on_click=reset_counter)

st.write("Feel free to increment the counter and see the cached results!")
