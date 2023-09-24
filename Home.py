import streamlit as st


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
