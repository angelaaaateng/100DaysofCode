import streamlit as st
from transformers import pipeline

print("**Successfully imported transformers library...")

st.set_page_config(page_title="Sentiment Analysis Tool", page_icon="🌍")

st.markdown("# Sentiment Analysis with HuggingFace")
st.sidebar.header("🤗 Sentiment Analysis")


sentiment_pipeline = pipeline("sentiment-analysis")

input_text = st.text_input("Write text to analyze here:", "I'm so incredibly happy I get to code today!")
st.markdown("### Sentiment using DistilBERT-base Uncased Finetuned SST 2 English")
st.write("The sentiment of the text is", sentiment_pipeline(input_text)[0]['label'], 
"with", sentiment_pipeline(input_text)[0]['score'], "probability.")
st.write("[HF Model Card](https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english?text=I+like+you.+I+love+you)")
st.write(sentiment_pipeline(input_text))

st.markdown("### Sentiment using BERTweet Base Model trained on SemEval 2017")
bert_tweet_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")
st.write("The sentiment of the text is", bert_tweet_model(input_text)[0]['label'], 
"with", bert_tweet_model(input_text)[0]['score'], "probability.")
st.write("[HF Model Card](https://huggingface.co/finiteautomata/bertweet-base-sentiment-analysis)")
st.write(bert_tweet_model(input_text))

st.markdown("### Sentiment using Twitter Roberta Base")
roberta_model = pipeline(model="cardiffnlp/twitter-roberta-base-sentiment")
st.write("The sentiment of the text is", roberta_model(input_text)[0]['label'], 
"with", roberta_model(input_text)[0]['score'], "probability.")
st.write("[HF Model Card](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment)")
st.write(roberta_model(input_text))
st.write("""Note that the labels for this model correspond to the following: \n
    - Label 0: Negative \n
    - Label 1: Neutral \n 
    - Label 2: Positive""")