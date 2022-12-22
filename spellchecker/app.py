import streamlit as st
from textblob import Word
from textblob import TextBlob
import re
from spellchecker import SpellChecker
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.metrics.distance  import edit_distance
from nltk.util import ngrams
# download correct words
nltk.download('words')
from nltk.corpus import words

st.title("100 Days of Natural Language Processing")
st.header("Creating a SpellCheck app in Python")
st.write("Accompanying documentation <a href='https://www.notion.so/angelateng/Day-1-Spellchecker-e8fb14f271494ddbb83fd5c42022b856'> here</a>")
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


def word_spellchecker(word_a):
    ''' 
    Function to Check word Spelling
    input: 
    - word: str for the input word
    output: 
    - probabilities[0][0]: str for the corrected word
    '''
    word_input = Word(word_a)
    probabilities = word_input.spellcheck() 
    if word_input == probabilities[0][0]:
        # if the input word is same as the output word, then it is correct
        st.write("The spelling of the word is already correct: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        return(word_input)
    else:
        print("Corrected Spelling: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        st.write("Corrected Spelling: ", probabilities[0][0], "with ", probabilities[0][1]*100, "percent confidence.")
        return(probabilities[0][0])

words_in_sentence = wrong_sentence.split()
print("Wrong sentence:", words_in_sentence)
words_in_sentence = [word.lower() for word in words_in_sentence]
words_in_sentence = [re.sub(r'[^A-Za-z0-9]+', '', word) for word in words_in_sentence]
for word in words_in_sentence: 
    st.write(word_spellchecker(word))

st.header("Spellcheck using Levenshtein Distance")
spell = SpellChecker()
misspelled = spell.unknown(words_in_sentence)
for word in misspelled:
    # Get the one `most likely` answer
    st.write(spell.correction(word))
    # Get a list of `likely` options
    st.write(spell.candidates(word))

st.header("Spellcheck using Jaccard Distance")
correct_words = words.words()

# loop for finding correct spellings
# based on jaccard distance
# and printing the correct word
# st.write("Words in sentence:", wrong_sentence.split())
for word in wrong_sentence.split():
    # change to 1-gram because the sentences are quite short
    temp = [(jaccard_distance(set(ngrams(word, 1)),
                              set(ngrams(w, 1))),w)
            for w in correct_words if w[0]==word[0]]
    st.write("The corrected word is:", sorted(temp, key = lambda val:val[0])[0][1])

st.header("Spellcheck using Edit Distance")
for word in wrong_sentence.split():
    temp = [(edit_distance(word, w),w) for w in correct_words if w[0]==word[0]]
    st.write("The corrected word is:", sorted(temp, key = lambda val:val[0])[0][1])