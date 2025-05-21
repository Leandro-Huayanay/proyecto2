import streamlit as st
import random

# Título de la app
st.title("Ecuaciones de primer grado: ¡Resuélvelas!")

# Función para generar una ecuación de primer grado aleatoria: ax + b = c
def generar_ecuacion():
    a = random.randint(1, 10)
    b = random.randint(-10, 10)
    x = random.randint(-10, 10)
    c = a * x + b
    return a, b, c, x

# Estado de sesión para mantener la ecuación
if "a" not in st.session_state:
    st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.respuesta_correcta = generar_ecuacion()

# Mostrar ecuación
a = st.session_state.a
b = st.session_state.b
c = st.session_state.c
st.latex(f"{a}x {'+' if b >= 0 else '-'} {abs(b)} = {c}")

# Entrada de usuario
respuesta_usuario = st.number_input("Introduce el valor de x:", step=1.0)

# Botón para verificar
if st.button("Verificar respuesta"):
    if respuesta_usuario == st.session_state.respuesta_correcta:
        st.success("✅ ¡Correcto!")
    else:
        st.error(f"❌ Incorrecto. La respuesta correcta era x = {st.session_state.respuesta_correcta}")

# Botón para generar nueva ecuación
if st.button("Generar nueva ecuación"):
    st.session_state.a, st.session_state.b, st.session_state.c, st.session_state.respuesta_correcta = generar_ecuacion()
    st.experimental_rerun()
