
import numpy as np
import pickle
import streamlit as st
from sklearn.neighbors import NearestNeighbors


st.header("Book Recommendation System")

suggest = pickle.load(open('suggest.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))
name = st.text_input("Find your favorites books ")


def recommendBook(book_name):
    books = []

    book_id = np.where(suggest.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(suggest.iloc[book_id, :].values.reshape(1, -1))

    for i in range(len(suggestions)):
        books = suggest.index[suggestions[i]]

    return books


if st.button("find books"):
    try:

        books = recommendBook(name)
        for i in range(1, len(books)):
            st.info(books[i])

    except:
        st.error("Invalid fields")
