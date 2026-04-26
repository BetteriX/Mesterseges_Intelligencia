#!/usr/bin/env python3

import streamlit as st
import csv
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


# 1. Betöltöm az adatszerkezetett
def load_dataset(file_name: str, text_row: str, label_row: str):
    texts = []
    labels = []

    with open(file_name, encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            text = row[text_row]
            label_num = int(row[label_row])

            texts.append(text)
            labels.append(label_num)

    return texts, labels


texts, labels = load_dataset("spam_ham_dataset.csv", "text", "label_num")

# 2. Szöveg vektorizálás és modell tanítása
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# 3. Streamlit app
st.title("Spam vagy Ham?")

user_input = st.text_area("Írj be egy üzenetet:")

if user_input:
    input_vector = vectorizer.transform([user_input])
    prediction = model.predict(input_vector)[0]
    proba = model.predict_proba(input_vector)[0]

    if prediction == 1:
        st.error(f"SPAM ({proba[1] * 100:.1f}%)")
    else:
        st.success(f"HAM ({proba[0] * 100:.1f}%)")
