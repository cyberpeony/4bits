import streamlit as st
import openai
import os

#Estilos de la pagina
st.markdown(
    """
    <style>
    %s
    </style>
    """ % open("ChatStyles.css").read(),
    unsafe_allow_html=True
)
#-------------------------

#Mental health related keywords:
mental_health_keywords = ["anxiety", "depression", "stress", "therapy"]

def is_mental_health_related(input_text):
    input_text = input_text
    return any(keyword in input_text for keyword in mental_health_keywords)


openai_api_key = st.secrets.openai.OPENAI_API_KEY   
openai.api_key = openai_api_key

messages = [
    {"role": "system", "content": "Entiendo que estés pasando por un momento difícil. Por favor, espera un momento y te conectaré con alguien que pueda ayudarte. Es importante mencionar que soy un intermediario y no tengo la capacidad de entender o responder a situaciones complejas como un ser humano. Si sientes que estás en peligro inmediato, por favor, contacta a las autoridades locales o busca atención médica urgente."},
]

message = st.chat_input("¿Cómo te sientes?: ")

#if is_mental_health_related(message):

if message:
    messages.append(
        {"role": "user", "content": message}
    )
    
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message.content
    #st.write(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})

    for message in messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
#else:
#    st.text("Please enter a mental health-related question.")

st.title("AuroraBot")


