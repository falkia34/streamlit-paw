import streamlit as st
import time

st.set_page_config(
    page_title="Calculation - Streamlit App",
    page_icon="🔥",
)

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
