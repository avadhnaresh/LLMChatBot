
from dotenv import load_dotenv
import os

load_dotenv()  # loads .env file

api_key = os.getenv("GROQ_API_KEY")
from groq import Groq


client = Groq(
    api_key=api_key
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)