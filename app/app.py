import streamlit as st
from src.summarizer import Summarizer

## streamlit app
st.set_page_config(page_title="ContentCrunch")
st.title("ContentCrunch: A GenAI based Youtube Content and Website Summarizer")
st.subheader("Summarize")
summarizer = Summarizer()

with st.sidebar:
    st.header("Input Parameters")
    model_name = st.text_input("Model Name", "Gemma-7b-It")
    temperature = st.slider("Temperature", 0.1, 1.0, 0.7, 0.1)

url = st.text_input("URL", "www.example.com/")
if st.button("Summarize"):
    st.spinner("Summarizing")
    summary = summarizer.summarize(url, model_name, temperature)
    st.success(summary)
