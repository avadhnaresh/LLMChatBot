from dotenv import load_dotenv
import os
import streamlit as st
from groq import Groq

from PyPDF2 import PdfReader  # for pdf reader in python



load_dotenv()  # loads .env file
api_key = os.getenv("GROQ_API_KEY") # key save in loca variable for security purpose 
st.title("document processing chatbot")  # title initilize

uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf"])  # we uploaded two format text and pdf

if uploaded_file:
    if uploaded_file.type=="text/plain": # what ever the data we retrive from pdf in text format
        file_content=uploaded_file.read().decode("utf-8")  #this is for reading data in human readable format


    elif uploaded_file.type=="application/pdf":   #this is for reading pdf 
        reader=PdfReader(uploaded_file) 
        text=""
        for page in reader.pages:
            text+=page.extract_text()

        
        file_content=text
    st.success("file uploade succesfully")
client = Groq(  # brog client for server
    api_key=api_key
)
question = st.text_input("ask me anything regarding file")

if st.button("submit"):  #for click button
    if question:  
        prompt=f"""answer the question based on the context below.
        context:{file_content}
        question:{question} """

        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{prompt}",
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        ans=chat_completion.choices[0].message.content
        st.write(ans) 
