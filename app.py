import streamlit as st
import pickle

import nltk
from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer

@st.cache_resource
def load_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

load_nltk()

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y = []

    stop_words = set(stopwords.words('english'))

    for i in text:
        if i not in stop_words and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y = []

    ps = PorterStemmer()
    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMS Spam Classifier')

input_sms = st.text_area("Enter the message")

if st.button('PREDICT'):
    #1. preprocessing
    transformed_sms = transform_text(input_sms)

    #2. Vectorize
    vector_input = tfidf.transform([transformed_sms]).toarray()

    #3. predict
    result = model.predict(vector_input)[0]


    #display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not spam")
