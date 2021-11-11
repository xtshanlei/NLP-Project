import spacy_streamlit
import streamlit as st
models = ['en_core_web_trf']
nlp = spacy.load('en_core_web_trf')
texts = st.text_area('Please type your texts here.')
spacy_streamlit.visualize(models, texts)
