# streamlit run streamlit_basic.py
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

with st.sidebar:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    model_ver = os.getenv("MODEL_VER")

st.title("🗨️ Chatbot")
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Let's start chatting! 👇"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])

# Accept user input
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    st.chat_message("user").write(prompt)
    
    response = client.chat.completions.create(model=model_ver, messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
