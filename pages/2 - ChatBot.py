import streamlit as st
import openai
import os

openai.api_key = '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'

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]



message = st.text_input("User: ")

if message:
    messages.append(
        {"role": "user", "content": message}
    )
    
    # Assuming you have your API key setup and openai properly imported
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    st.write(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


# Load OpenAI API key from secrets
#OPENAI_API_KEY = "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"#st.secrets["my_secret"]["OPENAI_API_KEY"]

# Set OpenAI API key
#openai.api_key = "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"#st.secrets["my_secret"]["OPENAI_API_KEY"]

# ... Rest of your Streamlit app code ...

st.title("ChatGPT-like clone")

# Set OpenAI API key from Streamlit secrets
#openai.api_key = st.secrets["OPENAI_API_KEY"]
