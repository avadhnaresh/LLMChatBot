
#this folder is for chat gpt
import streamlit as st
st.title("llmchatbox")  # title initilize


from dotenv import load_dotenv #load for .env
import os 

load_dotenv()  # loads .env file

api_key = os.getenv("GROQ_API_KEY") # key save in loca variable for security purpose 
from groq import Groq  #import gr0q


client = Groq(
    api_key=api_key
)

query = st.text_input("ask you anything")





if st.button("submit"):
    if query:
       
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": f"{query}",
                }
            ],
            model="llama-3.3-70b-versatile",
        )
        ans=chat_completion.choices[0].message.content
        st.write(ans) 

        