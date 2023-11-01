import streamlit as st
from display import display_text_analysis
import pandas as pd

def main():
    st.title("Text Analysis App")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        display_text_analysis(data)

if __name__ == "__main__":
    main()
