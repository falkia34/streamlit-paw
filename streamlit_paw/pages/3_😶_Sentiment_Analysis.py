import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import requests

API_URL = "https://api-inference.huggingface.co/models/ayameRushia/bert-base-indonesian-1.5G-sentiment-analysis-smsa"
headers = {"Authorization": "Bearer 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"}

st.set_page_config(
    page_title="Sentiment Analysis - Streamlit App",
    page_icon="🔥",
)


def main():
    st.title(":no_mouth: Sentiment Analysis")

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


if __name__ == '__main__':
    main()
