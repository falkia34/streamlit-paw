import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests
import plotly.express as px
from PIL import Image
from streamlit_navigation_bar import st_navbar


API_URL = "https://api-inference.huggingface.co/models/ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa"
API_TOKEN = st.secrets["HF_TOKEN"]

st.set_page_config(
    page_title="Sentiment Analysis - Streamlit App",
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
                 "Regression", "About"], selected="Sentiment Analysis", styles=styles)

if page == "Home":
    st.switch_page("0_🏠_Home.py")
if page == "Statistics":
    st.switch_page("pages/1_📊_Statistics.py")
if page == "Calculation":
    st.switch_page("pages/2_🔢_Calculation.py")
if page == "Regression":
    st.switch_page("pages/4_📈_Linear_Regression.py")
if page == "About":
    st.switch_page("pages/5_🔣_About.py")

st.title(":no_mouth: Sentiment Analysis")


def main():
    menu = ["English", "Indonesia"]
    choice = st.sidebar.selectbox("Language", menu)

    if choice == "English":
        with st.form("nlpForm"):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label='Analyze')

        # layout
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Results")
                sentiment = TextBlob(raw_text).sentiment
                st.write(sentiment)

                # Emoji
                if sentiment.polarity > 0:
                    st.markdown("Sentiment: Positive :smiley: ")
                elif sentiment.polarity < 0:
                    st.markdown("Sentiment: Negative :angry: ")
                else:
                    st.markdown("Sentiment: Neutral � ")

                # Dataframe
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

                # Visualization
                c = alt.Chart(result_df).mark_bar().encode(
                    x='Metric',
                    y='Value',
                    color='Metric')
                st.altair_chart(c, use_container_width=True)

            with col2:
                st.info("Token Sentiment")
                token_sentiments = en_analyze_token_sentiment(raw_text)
                st.write(token_sentiments)

    if choice == "Indonesia":
        with st.form("nlpForm"):
            raw_text = st.text_area("Enter Text Here")
            submit_button = st.form_submit_button(label='Analyze')

        # layout
        col1, col2 = st.columns(2)
        if submit_button:
            with col1:
                st.info("Results")
                scores = id_query(raw_text)[0]
                sentiment = max(scores, key=lambda x: x["score"])["label"]

                # Emoji
                if sentiment == 'Positive':
                    st.markdown("Sentiment: Positive :smiley: ")
                elif sentiment == 'Negative':
                    st.markdown("Sentiment: Negative :angry: ")
                else:
                    st.markdown("Sentiment: Neutral � ")

            with col2:
                st.info("Token Sentiment")
                token_sentiments = id_analyze_token_sentiment(raw_text)
                st.write(token_sentiments)


def id_query(payload):
    headers = {"Authorization": "Bearer " + API_TOKEN}

    response = requests.post(API_URL, headers=headers,
                             json={"inputs": payload})
    return response.json()


def convert_to_df(sentiment):
    sentiment_dict = {'Polarity': sentiment.polarity,
                      'Subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(
        sentiment_dict.items(), columns=['Metric', 'Value'])

    return sentiment_df


def en_analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []

    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']

        if res > 0.1:
            pos_list.append([i, res])
        elif res <= -0.1:
            pos_list.append([i, res])
        else:
            neu_list.append(i)

    result = {'positives': pos_list,
              'negatives': neg_list, 'neutral': neu_list}

    return result


def id_analyze_token_sentiment(docx):
    pos_list = []
    neg_list = []
    neu_list = []

    for i in docx.split():
        scores = id_query(i)[0]
        res = max(scores, key=lambda x: x["score"])

        if res['label'] == 'Positive':
            pos_list.append([i, res['score']])
        elif res['label'] == 'Negative':
            neg_list.append([i, res['score']])
        else:
            neu_list.append([i, res['score']])

    result = {'positives': pos_list,
              'negatives': neg_list, 'neutral': neu_list}

    return result


def wpdrama_analysis():
    df = pd.read_csv("streamlit_paw/data/wpdrama_result.csv")
    img = Image.open('streamlit_paw/data/wpdrama_wordcloud.png')

    color_mapping = {
        'positive': 'blue',
        'neutral': 'lightblue',
        'negative': 'red'
    }

    st.subheader("WordPress vs WP Engine Drama")
    st.image(img)

    st.markdown("### The Story")
    st.video('https://www.youtube.com/watch?v=mc5P_082bvY')

    st.markdown("### The Stats")

    col1, col2 = st.columns(2)

    with col1:
        df['date'] = pd.to_datetime(
            df['created_at'], format="%a %b %d %H:%M:%S %z %Y").dt.strftime('%Y-%m-%d')
        df1 = df.groupby(['date', 'label']).size().reset_index()
        df1 = df1.sort_values(['date'], ascending=True)
        df1.rename(columns={0: 'count'}, inplace=True)

        fig1 = px.line(df1, x="date", y="count", color='label', width=600,
                       height=400, color_discrete_map=color_mapping).update_layout(title_text='Sentiment Trend')
        st.plotly_chart(fig1, use_container_width=True)

    with col2:
        sentiment_count = df.groupby(['label'])['label'].count()
        sentiment_count = pd.DataFrame(
            {'Sentiments': sentiment_count.index, 'sentiment': sentiment_count.values})
        fig2 = px.pie(sentiment_count, values='sentiment', names='Sentiments', width=550,
                      height=400, color_discrete_map=color_mapping).update_layout(title_text='Sentiment Distribution')
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### Positive Sentiment")
    st.write(df[df['label'] == 'positive'][['full_text', 'score']
                                           ].sort_values(['score'], ascending=False))

    st.markdown("### Negative Sentiment")
    st.write(df[df['label'] == 'negative'][['full_text', 'score']
                                           ].sort_values(['score'], ascending=True))

    st.markdown("### Netral Sentiment")
    st.write(df[df['label'] == 'neutral'][['full_text', 'score']])


if __name__ == '__main__':
    menu = ["Analyze", "WordPress Drama Analysis"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Analyze":
        main()
    elif choice == "WordPress Drama Analysis":
        wpdrama_analysis()
