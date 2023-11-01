def text_analysis_logic(data, selected_column):
    text_data = data[selected_column]

    unique_values = text_data.nunique()
    missing_values = text_data.isnull().sum()
    empty_strings = (text_data == '').sum()
    whitespace_rows = text_data.str.isspace().sum()
    lowercase_rows = text_data.str.islower().sum()
    uppercase_rows = text_data.str.isupper().sum()
    alphabetic_rows = text_data.str.isalpha().sum()
    numeric_rows = text_data.str.isnumeric().sum()
    mode_value = text_data.mode().iloc[0] if not text_data.empty else None

    analysis_data = {
        "Metric": ["Unique Values", "Missing Values", "Empty Strings", "Whitespace Rows",
                   "Lowercase Rows", "Uppercase Rows", "Alphabetic Rows", "Numeric Rows", "Mode Value"],
        "Value": [unique_values, missing_values, empty_strings, whitespace_rows,
                  lowercase_rows, uppercase_rows, alphabetic_rows, numeric_rows, mode_value]
    }

    return analysis_data
