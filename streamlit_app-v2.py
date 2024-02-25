import streamlit as st
import openai
import fitz  # PyMuPDF
import pandas as pd

# Access the OpenAI API key from Streamlit secrets
# Ensure your secrets are structured correctly in Streamlit Cloud
openai.api_key = st.secrets["OPENAI_API_KEY"]

def generate_script(prompt):
    try:
        response = openai.Completion.create(
          engine="text-davinci-003",  # Ensure this engine is available in your API plan
          prompt=prompt,
          temperature=0.7,
          max_tokens=1024,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        return response.choices[0].text.strip()
    except Exception as e:
        st.error(f"An error occurred while generating the script: {e}")
        return ""

def process_upload(uploaded_file):
    # Ensure the uploaded file is a PDF before proceeding
    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.getvalue()
        doc = fitz.open("pdf", pdf_bytes)
        text = ""
        for page in doc:
            text += page.get_text()
        info = "Extracted information from the audit report based on text analysis"
        return info
    else:
        st.error("Uploaded file is not a PDF. Please upload a valid PDF file.")
        return ""

def main():
    st.title('Video Sales Letter Script Generator')
    
    uploaded_file = st.file_uploader("Upload your website audit report", type=['pdf'])
    if uploaded_file is not None:
        info = process_upload(uploaded_file)
        if info:  # Proceed only if info extraction was successful
            prompt = f"Based on the following website audit report: {info}, generate a video sales letter script."
            if st.button('Generate Script'):
                script = generate_script(prompt)
                if script:  # Display the script only if generation was successful
                    st.text_area("Generated Script", value=script, height=300)
                    st.download_button("Download Script", script, file_name="video_sales_letter_script.txt")

if __name__ == "__main__":
    main()
