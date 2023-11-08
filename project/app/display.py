import pandas as pd 
import streamlit as st
from logics import text_analysis_logic

def display_text_analysis(data):
    st.header("Text Serie Analysis")
    text_columns = data.select_dtypes(include='object').columns.tolist()

    selected_column = st.selectbox("Select a text column", text_columns)

    if selected_column:
        st.subheader("Analysis Results for " + selected_column)

        analysis_data = text_analysis_logic(data, selected_column)

        # Display analysis results in a table
        st.table(pd.DataFrame(analysis_data))

        # Show a bar chart for the number of occurrences for each value
        value_counts = data[selected_column].value_counts().head(20).reset_index()
        value_counts.columns = ['index', 'values']
        
        st.subheader("Bar Chart for Value Occurrences")
        bar_chart = st.bar_chart(value_counts)
        
        # Display occurrences and percentages for top 20 values
        st.subheader("Occurrences and Percentage for Top 20 Values")
        percentages = (value_counts['values'] / value_counts['values'].sum()) * 100
        occurrences_and_percentages = pd.concat([value_counts['index'], value_counts['values'], percentages], axis=1)
        occurrences_and_percentages.columns = ['Value', 'Occurrences', 'Percentage']
        st.table(occurrences_and_percentages)


