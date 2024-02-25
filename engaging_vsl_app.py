import streamlit as st
import openai
import requests

# Define the API endpoint URL
api_url = "https://chat.openai.com/g/g-PKxBCIZir-vsl-script-writer"

# Access the OpenAI API key from Streamlit secrets (ensure this is set in your Streamlit app's settings)
openai.api_key = st.secrets["secrets"]["OPENAI_API_KEY"]

def get_gpt_response(prompt):
    # Prepare the data to send to the API
    data = {"prompt": prompt}
    
    # Send a POST request to the API
    response = requests.post(api_url, json=data)
    
    # Debugging output
    print("Status Code:", response.status_code)
    print("Response Body (first 500 chars):", response.text[:500])
    
    if response.headers['Content-Type'] == 'application/json':
        try:
            response_data = response.json()
            return response_data.get("response", "No response key found in JSON.")
        except ValueError as e:
            st.error(f"Failed to decode JSON: {e}")
    else:
        st.error(f"Unexpected content type: {response.headers['Content-Type']}")
        # For debugging: Show the first part of the response body
        st.error(f"Response Body (for debugging): {response.text[:500]}")
    return ""

# Streamlit UI
st.title("Custom VSL Script Writer GPT Interface")
user_prompt = st.text_input("Enter your prompt:", "")

if st.button("Generate"):
    gpt_response = get_gpt_response(user_prompt)
    st.text_area("GPT Response:", value=gpt_response, height=200)
