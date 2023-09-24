import streamlit as st
import openai
import os

#Estilos de la pagina ----------------------------------------------------------
st.markdown(
    """
    <style>
    .circle {
        background-color: #89CFF0;
        color: #89CFF0;
        border-radius: 40%;
        padding: 10px;
        display: flex; /* Usa flexbox para organizar elementos en fila */
        font-weight: bold;
        font-size: 36px;
    }
    .circle img {
        border-radius: 80%;
        max-width: 80px; /* Establece el ancho máximo de la imagen */
        margin-right: 15px; /* Espacio entre la imagen y el título */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Contenedor para el círculo con la imagen y el título
st.markdown('<div class="circle"><img src="https://us.123rf.com/450wm/jemastock/jemastock1705/jemastock170505755/77918771-mujer-an%C3%B3nima-con-dise%C3%B1o-largo-del-ejemplo-del-vector-de-la-imagen-del-icono-del-pelo.jpg?ver=6" alt="Imagen" /><h1>AuroraBot</h1></div>', unsafe_allow_html=True)

st.markdown("""
     <div style="background-color: #FFD1DC; padding: 10px 20px; color: #494949; border-radius: 10px;">
   Texto de prueba 
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    /* Establece el color del texto en rojo (#FF0000) */
    .custom-chat-input input[type="text"] {
        color: #FF0000;
    }
    </style>
    """,
    unsafe_allow_html=True
)
#-----------------------------------------------------------------------------------------------------


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

message = st.chat_input("¿Cómo te sientes?: ", key="custom-chat-input")

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




