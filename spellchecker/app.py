import streamlit as st
from textblob import Word
from textblob import TextBlob
import re

st.title("100 Days of Natural Language Processing")

st.header("Spellcheck using TextBlob")

# spellcheck a single word
wrong_word = st.text_input('Please enter the word to spellcheck:', 'aple')
word_form = Word(wrong_word)
corrected_word = word_form.correct()
st.write("The corrected word is: ", corrected_word)
st.subheader("Spellcheck Probabilities")
# TO DO: Fix the format here so it isn't so ugly
st.write(word_form.spellcheck()[0:6])

# spellcheck a whole paragraph or sentence
wrong_sentence = st.text_area('Please enter the sentence you wish to spellcheck:', 'I ccant spellz')
wrong_sentence_tb = TextBlob(wrong_sentence)
corrected_sentence = wrong_sentence_tb.correct() 
st.write("The corrected sentence is: ", corrected_sentence)


def word_spellchecker(word):
    ''' 
    Function to Check word Spelling
    input: 
    - word: str for the input word
    output: 
    - probabilities[0][0]: str for the corrected word
    '''
    word = Word(word)
    probabilities = word.spellcheck() 
    if word == probabilities[0][0]:
        # if the input word is same as the output word, then it is correct
        st.write("The spelling of the word is already correct: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        return(word)
    else:
        print("Corrected Spelling: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        st.write("Corrected Spelling: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        return(probabilities[0][0])

words_in_sentence = wrong_sentence.split()
words = [word.lower() for word in words_in_sentence]
words = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words]
for word in words: 
    st.write(word_spellchecker(word))