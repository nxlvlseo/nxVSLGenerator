import streamlit as st
import openai
import fitz  # PyMuPDF
import pandas as pd

# Access the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["secrets"]["OPENAI_API_KEY"]

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

def process_upload(uploaded_file):
    # Convert Streamlit's UploadedFile to bytes
    pdf_bytes = uploaded_file.getvalue()
    
    # Open the PDF with fitz using the bytes
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    
    # Process the extracted text to find the information you need
    info = "Extracted information from the audit report based on text analysis"
    return info

def main():
    st.title('Video Sales Letter Script Generator')
    
    uploaded_file = st.file_uploader("Upload your website audit report", type=['csv', 'txt', 'pdf'])
    if uploaded_file is not None:
        info = process_upload(uploaded_file)
        prompt = f"You are an expert video sale letter copywriter. Based on the following website audit report: {info}, generate a Video Sales Letter script (VSL). Use the following guidelines to develop the script
        1. Opening Hook:
            Start with a strong, attention-grabbing statement or question that immediately addresses a common pain point or goal related to website performance. For instance, 'Did you know that 90% of online businesses overlook critical flaws in their websites that could be costing them thousands in lost revenue?'

        2. Introduction:
            Briefly introduce yourself and your company, emphasizing your expertise in website audit analysis and your success in helping businesses improve their online presence.

        3. Problem Identification:
            Highlight common problems and pain points that businesses face with their websites, such as poor user experience, low search engine rankings, or ineffective content strategy.

        4. Storytelling:
            Share a relatable story of a client who was struggling with their website until they used your audit analysis service, which dramatically improved their site's performance and business outcomes.

        5. Solution Presentation:
            Introduce your website audit analysis service as the solution to the problems mentioned. Detail how it works, what it examines (e.g., SEO, usability, content quality), and the value it provides.

        6. Unique Selling Proposition (USP):
            Explain what sets your service apart from others. This could be your comprehensive analysis, personalized improvement recommendations, or your track record of success.

        7. Proof Elements:
            Include testimonials, case studies, or statistical evidence that showcases the effectiveness of your service and the positive impact it has had on clients' businesses.

        8. Benefits:
            Focus on the benefits of your service, such as increased traffic, higher conversion rates, improved user engagement, and ultimately, more revenue.

        9. Offer Details:
            Clearly outline what your website audit analysis service includes, any bonuses or extras, and the terms of the offer (e.g., turnaround time, pricing, support).

        10. Guarantee:
            Offer a satisfaction guarantee or a money-back guarantee to mitigate risk and build trust with your audience.

        11. Call to Action (CTA):
            Encourage viewers to take the next step, such as signing up for a free initial consultation, booking a discovery call, or visiting your website to learn more about the service.

        12. Scarcity:
            Mention any limitations on availability (e.g., 'limited to the first 20 businesses this month') or special pricing for a limited time to create urgency.

        13. Closing Argument:
            Reiterate the key benefits of your service and the potential cost of inaction, emphasizing the importance of a high-performing website for business success.

        14. Final CTA:
            End with a strong, clear call to action, restating what you want the viewer to do next."
        if st.button('Generate Script'):
            script = generate_script(prompt)
            st.text_area("Generated Script", value=script, height=300)
            st.download_button("Download Script", script, file_name="video_sales_letter_script.txt")

if __name__ == "__main__":
    main()
