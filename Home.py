import streamlit as st
import os
import uuid
from supabase import create_client, Client
import time


#Estilos de la pagina

#-------------------------

# SUPABASE create_client + create_user + sign_user
url: str = st.secrets.supabase.SUPABASE_URL
key: str = st.secrets.supabase.SUPABASE_KEY
supabase: Client = create_client(url, key)
    
# streamlit run /workspaces/4bits/Home.py
st.header("Hola, la ayuda está en camino...")
st.subheader("Mientras, ayúdanos respondiendo 3 preguntas para brindarte el mejor apoyo posible:")
numero = st.text_input("Proporciona tu número de celular")
q1 = st.radio("En este momento, ¿estás experimentando pensamientos intensos o incontrolables de hacerle daño a ti mismo o de quitarte la vida?",["No","Sí"])
q2 = st.radio("¿Tienes acceso inmediato a cualquier método o medio que te permitiría causarte daño o suicidarte?",["No","Sí"])
q3 = st.radio("¿Hay alguien cerca de ti con quien te sientas seguro/a para hablar en este momento?",["Sí","No"])

def calcularRiesgo(q1,q2,q3):
    
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

        return total

    

def calculaPosicion():
    data = supabase.table("sessions").select("*").execute()
    return len(data.data) + 1
    #data = supabase.table("sessions").update({"position": newPosition}).execute()

def insertData():
    riesgo = calcularRiesgo(q1,q2,q3)
    st.write(riesgo)
    posicion = calculaPosicion()
    st.write(posicion)
    data = supabase.table("sessions").insert({"position":posicion,"risk_level":riesgo,"tel":numero}).execute()
    assert len(data.data) > 0

# def ordena_intercambio(totalSessions):
#     n = len(totalSessions)
#     for i in range(n - 1):
#         posicion_min = i
#         for j in range(i + 1, n):
#             if totalSessions[j] < totalSessions[posicion_min]:
#                 posicion_min = j

#         if posicion_min != i:
#             swap_temporal = totalSessions[i]
#             totalSessions[i] = totalSessions[posicion_min]
#             totalSessions[posicion_min] = swap_temporal

if st.button("Chatear",key = "botonUno"):
    insertData()
    # ordena_intercambio()
