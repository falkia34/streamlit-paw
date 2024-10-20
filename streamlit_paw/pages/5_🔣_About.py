import streamlit as st
from streamlit_navigation_bar import st_navbar

st.set_page_config(
    page_title="About - Streamlit App",
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
                 "Regression", "About"], selected="About", styles=styles, options=options)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
if page == "Calculation":
    st.switch_page("pages/2_🔢_Calculation.py")
if page == "Sentiment Analysis":
    st.switch_page("pages/3_😶_Sentiment_Analysis.py")
if page == "Regression":
    st.switch_page("pages/4_📈_Linear_Regression.py")

st.title(":symbols: About")

st.write("""
**Streamlit App** is a leading platform designed to empower individuals and organizations to make data-driven decisions. Founded in 2023 by a team of data enthusiasts and industry experts, our mission is to make data analysis accessible, intuitive, and actionable for everyone, regardless of their technical background.
""")

st.header("Our Mission")
st.write("""
Our mission is simple: to democratize data insights. We believe that data should not be confined to the hands of a few, but accessible to all. Whether you're an experienced data scientist or someone exploring data for the first time, **Streamlit App** provides the tools and resources you need to uncover valuable insights and make informed decisions.
""")

st.header("Our Story")
st.write("""
**Streamlit App** was born out of a need to simplify data analysis. Our founders, frustrated with the complexity and inaccessibility of existing data tools, set out to create a platform that is both powerful and easy to use. What started as a small project in a garage has grown into a robust platform trusted by thousands of users around the world.

Over the years, we've expanded our capabilities, integrated the latest technologies, and continuously improved our platform based on user feedback. Today, **Streamlit App** is at the forefront of the data revolution, helping individuals and businesses transform data into actionable insights.
""")

st.header("Our Values")
st.write("""
- **Accessibility:** We believe that everyone should have access to powerful data analysis tools, regardless of their background or experience.
- **Innovation:** We are committed to continuous improvement and staying ahead of the curve with the latest data technologies.
- **Collaboration:** We foster a community where users can share insights, collaborate on projects, and learn from each other.
- **Transparency:** We operate with integrity and ensure that our users have full control over their data.
""")

st.header("Meet the Team")
st.write("""
Our team is made up of data scientists, engineers, and designers who are passionate about making data analysis accessible to all. We come from diverse backgrounds, bringing together expertise in data science, software development, and user experience design.

- **Emma Johnson** - CEO & Co-Founder: Emma is a visionary leader with over a decade of experience in the data industry. She is passionate about democratizing data and making complex concepts easy to understand.
- **Liam Brown** - CTO & Co-Founder: Liam is the technical brain behind Streamlit App. With a background in software engineering and data science, he ensures that our platform is always at the cutting edge of technology.
- **Sophia Martinez** - Head of Product: Sophia oversees the development and design of our products. Her focus is on creating intuitive and user-friendly interfaces that make data analysis a breeze.
- **Noah Wilson** - Head of Customer Success: Noah leads our customer support team, ensuring that users have a seamless experience and get the most out of our platform.
""")

st.header("Join Our Community")
st.write("""
**Streamlit App** is more than just a tool; it's a community. Join our growing community of data enthusiasts, professionals, and learners. Share your insights, ask questions, and collaborate on projects.

- [Join our Slack Community](#)
- [Follow us on Twitter](#)
- [Subscribe to our Newsletter](#)
""")

st.header("Contact Us")
st.write("""
Have any questions or want to learn more about our platform? Feel free to reach out to us!

- **Email:** [contact@streamlit.app](mailto:contact@streamlit.app)
- **Phone:** +1 (555) 123-4567
- **Address:** 123 Data Street, Suite 456, Data City, DS 78901
""")

st.write("Thank you for being a part of the **Streamlit App** journey. Together, we're making data accessible to everyone.")
