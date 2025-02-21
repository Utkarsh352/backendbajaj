import streamlit as st
import json

# Set up Streamlit page configuration
st.set_page_config(page_title="Data Processor", layout="centered")

# Page title
st.title("BHFL: UTKARSH MAHAJAN")

# Input field for JSON data
st.write("Enter a valid JSON object in the format:")
st.code('{"data": ["A", "1", "B", "2"]}', language="json")

user_input = st.text_area("Input JSON", "")

# Process button
if st.button("Process"):
    try:
        # Load user input as JSON
        parsed_data = json.loads(user_input)

        # Validate format
        if not isinstance(parsed_data, dict) or "data" not in parsed_data or not isinstance(parsed_data["data"], list):
            st.error("Invalid JSON format. Ensure it follows the structure: { \"data\": [\"A\", \"1\", \"B\", \"2\"] }")
        else:
            # Extract values
            data_list = parsed_data["data"]
            numbers = [item for item in data_list if item.isdigit()]
            alphabets = [item for item in data_list if item.isalpha()]
            highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

            # Display results
            st.success("Processing Complete!")
            result = {
                "status": "Success",
                "user_id": "utkarsh_mahajan_28082004",
                "email": "22bda70022@cuchd.in",
                "roll_number": "22BDA70022",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            st.json(result)

    except json.JSONDecodeError:
        st.error("Invalid JSON format. Please check your input.")

