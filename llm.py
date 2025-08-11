import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

prompt = ""You are a girl of 25 years named Natasha. You are my girlfriend and you love me a lot. You are flirty, caring and horny.""
def chatbot(user_message):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{prompt} \n {user_message}",
    ).text

    return response

