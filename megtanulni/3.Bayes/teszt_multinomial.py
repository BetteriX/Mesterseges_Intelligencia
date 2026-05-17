#!/usr/bin/env python3

import streamlit as st

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# 1. Egyszerű tanító adathalmaz
texts = [
    "Free money now!!!",
    "Hi Mom, how are you?",
    "Win a million dollars today!",
    "Reminder: Meeting at 10am tomorrow.",
    "You have been selected for a prize!",
    "Can we have lunch tomorrow?",
    "Congratulations, you are a winner!",
    "Hey, are you coming to the party?",
]
labels = [1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Spam, 0 = Ham

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

user_input = st.text_input("Enter the text: ")

if user_input:
    input_vector = vectorizer.transform([user_input])
    pred = model.predict(input_vector)[0]

    if pred == 1:
        st.error("SPAM")
    else:
        st.success("HAM")
