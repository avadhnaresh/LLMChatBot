import streamlit as st
st.title("llmchatbox")


from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

api_key = os.getenv("GROQ_API_KEY")
from groq import Groq


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

        