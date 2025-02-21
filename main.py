import streamlit as st
from flask import Flask, request, jsonify
from threading import Thread

# Initialize Flask App
flask_app = Flask(__name__)

# ✅ API Endpoint at /bfhl (Only Returns JSON)
@flask_app.route("/bfhl", methods=["POST"])
def process_data():
    try:
        # Get JSON input
        request_data = request.get_json()
        if not request_data or "data" not in request_data or not isinstance(request_data["data"], list):
            return jsonify({"is_success": False, "message": "Invalid JSON format"}), 400

        data_list = request_data["data"]

        # Separate numbers and alphabets
        numbers = [item for item in data_list if item.isdigit()]
        alphabets = [item for item in data_list if item.isalpha()]
        highest_alphabet = [max(alphabets, key=str.upper)] if alphabets else []

        # Create response
        response = {
            "is_success": True,
            "user_id": "utkarsh_mahajan_28082004",
            "email": "22bda70022@cuchd.in",
            "roll_number": "22BDA70022",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500

# ✅ GET Request for /bfhl (Returns JSON, No Frontend)
@flask_app.route("/bfhl", methods=["GET"])
def get_status():
    return jsonify({"operation_code": 1})

# Run Flask in a separate thread
def run_flask():
    flask_app.run(port=8000, debug=False, use_reloader=False)

# Start Flask in a background thread
flask_thread = Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

# ✅ Streamlit UI for Testing API
st.set_page_config(page_title="BFHL API & UI", layout="centered")
st.title("BFHL Data Processor")

st.subheader("Test the API")
st.write("### Submit JSON Data to `/bfhl` Endpoint")
st.code('{"data": ["A", "1", "B", "2"]}', language="json")

# User input field
user_input = st.text_area("Enter JSON here", "")

if st.button("Submit Request"):
    import requests
    try:
        headers = {"Content-Type": "application/json"}
        response = requests.post("http://127.0.0.1:8000/bfhl", json=eval(user_input), headers=headers)

        if response.status_code == 200:
            st.success("API Response:")
            st.json(response.json())
        else:
            st.error(f"Error {response.status_code}: {response.text}")

    except Exception as e:
        st.error(f"Invalid Input: {e}")
