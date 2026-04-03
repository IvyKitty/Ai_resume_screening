import streamlit as st 
from PyPDF2 import PdfReader
import pandas as pd 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# fuction to extract text from PDF 
def extract_text_from_pdf(file):
    pdf = PdfReader(file)
    text = ""
    for page in pdf.pages:
        text += page.extract_text()
    return text 


# function to rank resumes based on job description 
def rank_resumes(job_description, resumes):
    documents[job_description] + resumes
    vectorizer = TfidfVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()

    job_description_vector = vectors[0]
    resume_vectors = vectors [1:]
    cosine_similarities = cosine_similarity ([job_description_vector], resume_vectors).flatten()

    return cosine_similarities 


# streamlit app 
st.title("AI Resume Screening & Candidate Ranking System")
# job description input 
st.header("Job Description")
job_description = st.text_area("Enter the job Description")


# file uploader 
st.header("Upload Resumes")
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)



if uploaded_files and job_description:
    st.header("Ranking Resumes")

    resumes = []
    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        resumes.append(text)

   # rank resumes 
    scores = rank_resumes(job_description,resumes)

   # display scores 
    results = pd.Dataframe({"Resume":[file.name for file in uploaded_files], "Score": scores})
    results = results.sort_values(by="Score", acending=False)

    st.write(results)

