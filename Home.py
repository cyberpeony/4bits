import streamlit as st
import os
import uuid
from supabase import create_client, Client

#Estilos de la pagina
st.markdown(
    """
    <style>
    %s
    </style>
    """ % open("Home.css").read(),
    unsafe_allow_html=True
)

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

load_css('Home.css')
#-------------------------

# SUPABASE
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    url = st.secrets.supabase.SUPABASE_URL
    key = st.secrets.supabase.SUPABASE_KEY
    return create_client(url, key)

supabase = init_connection()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
# @st.cache_data(ttl=600)
#def run_query():
    #return supabase.table("mytable").select("*").execute()

#rows = run_query()

# Print results.
#for row in rows.data:
   #st.write(f"{row['name']} has a :{row['pet']}:")
   
email = st.text_input("Correo: ")
password = st.text_input("Contraseña: ")
res = supabase.auth.sign_up({
  "email": email,
  "password": password,
})


# data = supabase.auth.sign_in_with_password({"email": email, "password": password})



# streamlit run /workspaces/4bits/Home.py
st.header("Hola, la ayuda está en camino...")
st.subheader("Mientras, ayúdanos respondiendo 3 preguntas para brindarte el mejor apoyo posible:")
q1 = st.radio("En este momento, ¿estás experimentando pensamientos intensos o incontrolables de hacerle daño a ti mismo o de quitarte la vida?",["Sí","No"])
q2 = st.radio("¿Tienes acceso inmediato a cualquier método o medio que te permitiría causarte daño o suicidarte?",["Sí","No"])
q3 = st.radio("¿Hay alguien cerca de ti con quien te sientas seguro/a para hablar en este momento?",["Sí","No"])


if st.button("Chatear"):
    if q1 == "Sí":
        q1_int = 1
    else:
        q1_int = 0

    if q2 == "Sí":
        q2_int = 1
    else:
        q2_int = 0

    if q3 == "Sí":
        q3_int = 0
    else:
        q3_int = 1

    total = q1_int + q2_int + q3_int

    if total == 3:
        riesgo = "alto"
    elif total == 2:
        riesgo = "medio"
    elif total == 1:
        riesgo = "bajo"
