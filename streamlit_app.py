pip install openai
import streamlit as st
import openai
import pandas as pd

# Access the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["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"]

def generate_script(prompt):
    response = openai.Completion.create(
      engine="text-davinci-003",  # Update the engine if needed
      prompt=prompt,
      temperature=0.7,
      max_tokens=1024,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return response.choices[0].text.strip()

def process_upload(file):
    # Function to extract information from the uploaded file
    # Adjust according to the format and structure of your reports
    df = pd.read_csv(file)
    # Placeholder for your logic to extract information
    info = "Extracted information from the audit report"
    return info

def main():
    st.title('Video Sales Letter Script Generator')
    
    uploaded_file = st.file_uploader("Upload your website audit report", type=['csv', 'txt', 'pdf'])
    if uploaded_file is not None:
        info = process_upload(uploaded_file)
        prompt = f"Based on the following website audit report: {info}, generate a video sales letter script."
        if st.button('Generate Script'):
            script = generate_script(prompt)
            st.text_area("Generated Script", value=script, height=300)
            st.download_button("Download Script", script, file_name="video_sales_letter_script.txt")

if __name__ == "__main__":
    main()
