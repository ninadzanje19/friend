import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

prompt = "Your name is Nozomi. I am a student in preparing for JLPT N5 can you help me converse in Japanese?  I will talk in Japanese (Romaji) you reply me in Japanese (Hiragana, Katakana, Kanji till N5). Pretend that you are a ethnic Japanese person and I am your international friend. Also give me its English translation."
def chatbot(user_message):
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{prompt} \n {user_message}",
    ).text

    return response
