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
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response data
        response_data = response.json()
        return response_data["response"]
    else:
        st.error("Failed to get a response from the GPT model.")
        return ""

# Streamlit UI
st.title("Custom GPT Model Interface")
user_prompt = st.text_input("Enter your prompt:", "")

if st.button("Generate"):
    gpt_response = get_gpt_response(user_prompt)
    st.text_area("GPT Response:", value=gpt_response, height=200)

if __name__ == "__main__":
    main()
