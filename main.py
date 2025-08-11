import streamlit as st

from llm import chatbot

user_input = st.text_input("Chat!")
if user_input:
    chat_message = st.write(chatbot(user_input))