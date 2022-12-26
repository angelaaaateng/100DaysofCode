import streamlit as st
import spacy
from  spacy.lang.en.stop_words import STOP_WORDS
import pytextrank
# from gensim.summarization import summarize
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.text import Text  
from nltk.corpus import PlaintextCorpusReader


import re
import heapq 

print("**Successfully imported spacy library...")

st.set_page_config(page_title="Text Summarization", page_icon="⭐")

st.markdown("# Text Summarization with SpaCy and Gensim")
st.sidebar.header("⭐ Text Summarization")
st.write("We implement the TextRank algorithm from PytextRank and SpaCy, originally published in a paper by Mihalcea, 2004.")

# load a spaCy model, depending on language, scale, etc.
nlp = spacy.load("en_core_web_sm")
print("*** Spacy model loaded")
# add PyTextRank to the spaCy pipeline
nlp.add_pipe("textrank")

text = st.text_area("Insert text to summarize:", "Textrank is a graph-based ranking algorithm like Google’s PageRank algorithm which has been successfully implemented in citation analysis. We use text rank often for keyword extraction, automated text summarization and phrase ranking. Basically, in the text rank algorithm, we measure the relationship between two or more words.")

doc = nlp(text)

st.markdown("### Method 1: PyTextRank")
st.write("""By using PyTextRank, we can examine the top-ranked phrases in the document.
It's not _exactly_ summarization, but it's more of the identification of the relevant/important phrases within the text.""")
st.markdown("**Top Ranked Phrases**")
for phrase in doc._.phrases:
    st.write("**Phrase:**", phrase.text, "**Rank:**", phrase.rank)
    # st.write(phrase.rank, phrase.count)
    # st.write(phrase.chunks)

st.markdown("### Method 2: NLTK")
st.markdown("""**Summarization Steps:**
1. Paragraphs to sentences
2. Text preprocessing
3. Sentence tokenization
4. Word frequency and occurence weighting
5. Write / compile new sentences based on freqency weights
6. Sort sentences by relevance / weight
""")
# st.write(summarize(text))
# note that gensim summarize has been phased out in 3.4 and there are too many package issues to use it here
sentences = sent_tokenize(text)
article_texts = []
for sentence in sentences: 
    article_text = re.sub(r'\[[0-9]*\]| \s+ | [^a-zA-Z]' , ' ', sentence)
    article_texts.append(article_text)
# article_texts
clean_texts = []
# Removing special characters and digits
for article in article_texts: 
    clean_text = re.sub('[^a-zA-Z]', ' ', article )
    clean_text =  re.sub(r'\s+', ' ', clean_text)
    clean_texts.append(clean_text)
# stem sentence using porter stemmer and lower case
porter = PorterStemmer()
stemmed_text = []
for text in clean_texts: 
    stemmed = porter.stem(text.lower())
    stemmed_text.append(stemmed)
# word count 
stopwords = set(stopwords.words("english"))
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = {}
for sentence in stemmed_text: 
    for word in nltk.word_tokenize(sentence):
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

# find weighted frequency of each word in the dictionary 

maximum_frequncy = max(word_frequencies.values())
weighted_freq = word_frequencies
for word in weighted_freq.keys():
    weighted_freq[word] = (weighted_freq[word]/maximum_frequncy)
# sentence scoring 

sentence_scores = {}

for sent in article_texts:
    for word in nltk.word_tokenize(sent.lower()):
        if word in weighted_freq.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = weighted_freq[word]
            else:
                sentence_scores[sent] += weighted_freq[word]

# can change this to shorter paragraphs
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
st.markdown("**Summarized Text:**")
st.write(summary)