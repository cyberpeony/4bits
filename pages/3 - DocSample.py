import streamlit as st
import openai
import os
from supabase import create_client, Client
import time


# #Estilos de la pagina

# #-------------------------

# # SUPABASE create_client 
# url: str = st.secrets.supabase.SUPABASE_URL
# key: str = st.secrets.supabase.SUPABASE_KEY
# supabase: Client = create_client(url, key)
# openai_api_key = st.secrets.openai.OPENAI_API_KEY   
# openai.api_key = openai_api_key

# messages = [
#     {"role": "system", "content": " "},
# ]

# dataSesh = supabase.table("sessions").select("*").execute()
# assert len(dataSesh.data) > 0
# for i in range(len(dataSesh.data)):
#     if dataSesh.data[i].get
#     totalString = "Resumen de manera que un profesional de la salud pueda entender en 50 palabras el estado de la siguiente persona: "
#     data = supabase.table("commits").select("*").eq("tel", dataSesh.data[i].get("tel")).execute()
#     for i in range(len(data.data)):
#         totalString = totalString + "," + data.data[i].get("commit")
#     messages.append({"role": "assistant", "content": totalString})
# chat = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo", messages=messages
#     )
# reply = chat.choices[0].message.content