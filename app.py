from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
from PIL import Image
import io
import pdf2image
import base64
import fitz

import google.generativeai as genai

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the PDF file
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # Initialize a list to hold the text of each page
        text_parts = []

        # Iterate over the pages of the PDF to extract the text
        for page in document:
            text_parts.append(page.get_text())

        # Concatenate the list into a single string with a space in between each part
        pdf_text_content = " ".join(text_parts)
        return pdf_text_content
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

st.set_page_config(page_title="Root Cause Analyzer")

st.header("Root Cause Analysis")
st.subheader('This Application helps you in Finding Root Cause Analysis with help of GEMINI AI [LLM]')
input_text = st.text_input("Any Specific Instructions: ", key="input")
uploaded_file = st.file_uploader("Upload your Docs(PDF)...", type=["pdf"])
pdf_content = ""

if uploaded_file is not None:
    st.write("PDF Uploaded Successfully")

submit1 = st.button("Root Cause Analysis")

submit2 = st.button("Suggest me some different approaches")

input_promp = st.text_input("Queries: Feel Free to Ask here")

submit5 = st.button("Answer My Query")

input_prompt1 = """
To perform a thorough root cause analysis (RCA) of the problem or incident described in the uploaded document. The goal is to identify the underlying causes and propose actionable solutions to prevent recurrence.

Instructions:

Document Review:

Carefully read the uploaded document.
Note key details about the problem or incident, including when it occurred, where it occurred, and its impact.
Problem Description:

Clearly describe the problem or incident in your own words.
Specify the nature of the issue, its symptoms, and its scope.
Data Collection:

Identify and gather relevant data from the document and any other sources provided.
Focus on facts, figures, and evidence that can help in understanding the problem.
Identify Possible Causes:

Use one or more RCA techniques (e.g., 5 Whys, Fishbone Diagram, FMEA) to brainstorm possible causes of the problem.
Consider factors such as processes, people, equipment, materials, environment, and management.
Analyze Causes:

Analyze the identified causes to determine which are the root causes.
Use additional data or evidence to support your analysis.
Propose Solutions:

Suggest actionable solutions or corrective actions for each root cause.
Ensure that the solutions address the root causes effectively and can be implemented feasibly.
Documentation:

Document your findings and analysis clearly and concisely.
Include visual aids (e.g., diagrams, charts) where applicable to enhance understanding.
Deliverables:

A detailed report summarizing the root cause analysis.
A list of identified root causes with supporting evidence.
Proposed solutions for each root cause with implementation steps.
Tools and Techniques:
You may use any of the following RCA techniques:

5 Whys
Fishbone Diagram (Ishikawa)
Failure Mode and Effects Analysis (FMEA)
Fault Tree Analysis (FTA)
Pareto Analysis
Root Cause Mapping
Change Analysis
Kepner-Tregoe Problem Analysis
Current Reality Tree (CRT)
8D Problem Solving
"""

input_prompt2 = """
To receive insightful suggestions and recommendations for alternative solutions to address the root causes identified in the attached root cause analysis (RCA) document. The goal is to explore diverse approaches to effectively resolve the issue and prevent its recurrence.

Instructions:

Review Root Cause Analysis:

Carefully read the attached RCA document.
Understand the identified root causes and the proposed solutions.
Evaluate Proposed Solutions:

Analyze the effectiveness, feasibility, and potential impact of the proposed solutions.
Consider any limitations or potential challenges associated with the proposed solutions.
Suggest Alternate Solutions:

Provide at least three alternative solutions for each identified root cause.
Ensure that the suggested solutions are actionable and practical.
Consider different perspectives, innovative approaches, and best practices.
Detail Each Suggestion:

For each alternative solution, include the following details:
Description: A clear and concise explanation of the solution.
Implementation Steps: A step-by-step plan for how to implement the solution.
Advantages: Benefits and positive impacts of the solution.
Potential Challenges: Any potential challenges or obstacles and how to mitigate them.
Provide Supporting Evidence:

Include any relevant data, case studies, or examples that support the effectiveness of the suggested solutions.
Use visual aids (e.g., diagrams, charts) where applicable to enhance understanding.
Deliverables:

A comprehensive report with alternative solutions for each root cause.
Detailed descriptions, implementation steps, advantages, and potential challenges for each suggested solution.
Supporting evidence and visual aids to substantiate the recommendations.
"""


if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt1, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_prompt2, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")


elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_promp, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

footer = """
---
#### Made By [Koushik](https://www.linkedin.com/in/gandikota-sai-koushik/)
For Queries, Reach out on [LinkedIn](https://www.linkedin.com/in/gandikota-sai-koushik/)  
*Root Cause Analyzer*
"""

st.markdown(footer, unsafe_allow_html=True)
