import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="Home - Streamlit App",
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
                 "Regression", "Image Classification", "About"], styles=styles, options=options)

if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
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

st.title(":house: Home")

st.write("""
**Streamlit App** is your one-stop destination for exploring data, visualizing trends, and gaining insights from various datasets. Whether you're a data enthusiast, a professional analyst, or someone just curious about data, our platform provides you with the tools and visualizations you need to uncover the stories hidden within the numbers.
""")

st.header("Why Choose Streamlit App?")
st.write("""
- **User-Friendly Interface:** Navigate through our clean and intuitive interface to find the data and insights you need with ease.
- **Comprehensive Analysis:** From basic statistics to advanced visualizations, our platform offers a wide range of tools to analyze your data.
- **Real-Time Data:** Access the latest datasets and monitor changes as they happen with our real-time data integration.
- **Customizable Dashboards:** Tailor your data visualizations to your specific needs with our flexible dashboard options.
""")

st.header("Key Features")
st.write("""
- **Interactive Visualizations:** Use our interactive charts and graphs to explore data in new and engaging ways.
- **Data Export Options:** Download your data and visualizations in various formats for use in reports or presentations.
- **Collaboration Tools:** Share your insights with colleagues and collaborate on data analysis projects in real time.
- **Secure Data Handling:** Your data's security is our top priority. We use the latest encryption and security protocols to protect your information.
""")

st.header("What Our Users Say")
st.write("""
> "Streamlit App has transformed the way we analyze our data. The platform's ease of use and powerful features have made it an invaluable tool for our team."
> — Sarah K., Data Analyst

> "I love the customizable dashboards! Being able to visualize our data exactly how we need it has been a game changer."
> — John D., Business Intelligence Manager

> "The real-time data integration keeps us ahead of the curve. We can make informed decisions faster than ever before."
> — Emily R., Marketing Director
""")

st.header("Get Started")
st.write("""
Ready to dive in? Use the sidebar to navigate to the **Statistics** page and explore some sample data. If you're new here, head over to the **About** page to learn more about what we offer.
""")

st.write("""
Have questions or need support? [Contact Us](mailto:support@streamlit.app) or visit our [Help Center](#).
""")

st.write("Thank you for choosing **Streamlit App** – where data meets discovery.")
