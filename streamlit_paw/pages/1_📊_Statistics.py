import streamlit as st
import numpy as np
import pandas as pd
import time
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="Statistics - Streamlit App",
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
                 "Regression", "Image Classification", "About"], selected="Statistics", styles=styles)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Calculation":
    st.switch_page("pages/2_🔢_Calculation.py")
if page == "Sentiment Analysis":
    st.switch_page("pages/3_😶_Sentiment_Analysis.py")
if page == "Regression":
    st.switch_page("pages/4_📈_Linear_Regression.py")
if page == "Image Classification":
    st.switch_page("pages/5_👻_Bisindo_Gesture.py")
if page == "About":
    st.switch_page("pages/6_🔣_About.py")

st.title(":bar_chart: Statistics")

# Create a random DataFrame for demonstration


def generate_random_data():
    np.random.seed(42)
    data = np.random.randn(1000, 4)
    columns = ['Sales', 'Profit', 'Expenses', 'Customer Satisfaction']
    return pd.DataFrame(data, columns=columns)


st.write("Explore the detailed statistics and insights from the dataset.")

# Sidebar controls
st.sidebar.header("Filter Data")
show_data = st.sidebar.checkbox("Show Raw Data")
show_summary = st.sidebar.checkbox("Show Summary Statistics", value=True)
show_visualization = st.sidebar.checkbox("Show Visualizations", value=True)
num_rows = st.sidebar.slider(
    "Number of Rows to Display", min_value=5, max_value=100, value=10)

# Generate random data
data = generate_random_data()

# Display raw data
if show_data:
    st.subheader("Raw Data")
    st.write("Here's a preview of the dataset:")
    st.dataframe(data.head(num_rows))

# Display summary statistics
if show_summary:
    st.subheader("Summary Statistics")
    st.write("The following table summarizes the dataset:")
    st.table(data.describe())

# Display visualizations
if show_visualization:
    st.subheader("Data Visualizations")
    st.write("Below are some key visualizations of the dataset:")

    # Line chart
    st.write("### Sales and Profit Over Time")
    st.line_chart(data[['Sales', 'Profit']])

    # Area chart
    st.write("### Expenses Over Time")
    st.area_chart(data['Expenses'])

    # Bar chart
    st.write("### Average Metrics")
    avg_metrics = data.mean()
    st.bar_chart(avg_metrics)

    # Map (for geographic data - dummy implementation)
    st.write("### Customer Satisfaction - Geographic Distribution")
    st.write(
        "This is a dummy map visualization since we're not using real geographic data.")
    df_map = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
        columns=['lat', 'lon'])
    st.map(df_map)

# Download button for data
st.subheader("Download Data")
st.write("Download the dataset for your own analysis.")
csv = data.to_csv(index=False)
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='random_data.csv',
    mime='text/csv',
)

# Expander for additional insights
with st.expander("Additional Insights"):
    st.write("Here are some additional insights based on the data:")
    st.write("""
    - **Highest Sales:** Month 7, with a peak of $120,000.
    - **Lowest Profit Margin:** Month 3, with a margin of only 10%.
    - **Top Expenses Category:** Marketing, contributing to 35% of the total expenses.
    - **Customer Satisfaction:** Consistently above 80% across all quarters.
    """)

# Progress bar (for long-running computations)
st.subheader("Long-Running Computation Example")
st.write("Simulating a long-running computation:")
progress_bar = st.progress(0)
status_text = st.empty()

for i in range(100):
    progress_bar.progress(i + 1)
    status_text.text(f"Processing... {i+1}% complete")
    time.sleep(0.05)

st.success("Computation completed successfully!")

# File uploader (for user-provided data)
st.subheader("Upload Your Own Dataset")
st.write("Want to analyze your own data? Upload a CSV file below.")
uploaded_file = st.file_uploader("Choose a file", type="csv")
if uploaded_file is not None:
    user_data = pd.read_csv(uploaded_file)
    st.write("Here's a preview of your uploaded data:")
    st.dataframe(user_data.head())

st.subheader("Uber Pickups in NYC")

DATE_COLUMN = 'date/time'
DATA_URL = (
    'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Func. for loading the data


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Get data
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache_data)")

# Show and Hide DataFrame
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Adding Histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.bar_chart(hist_values)

# Map filters based on the hour filter
# Some number in the range 0-23
hour_to_filter = st.slider('Hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# Show the map
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
