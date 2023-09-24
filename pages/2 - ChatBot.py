import streamlit as st
import openai
import os
from supabase import create_client, Client


openai_api_key = st.secrets.openai.OPENAI_API_KEY   
openai.api_key = openai_api_key

messages = [
    {"role": "system", "content": "You are a kind helpful assistant."},
]

message = st.text_input("User: ")

if message:
    messages.append(
        {"role": "user", "content": message}
    )
    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    st.write(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})


st.title("AuroraBot")

# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets.supabase.SUPABASE_URL
    key = st.secrets.supabase.SUPABASE_KEY
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query():
    return supabase.table("mytable").select("*").execute()

rows = run_query()

# Print results.
for row in rows.data:
    st.write(f"{row['name']} has a :{row['pet']}:")