import streamlit as st

def contar_letra(parrafo, letra):
    parrafo = parrafo.lower()
    letra = letra.lower()
    return parrafo.count(letra)

def contar_todas_las_letras(parrafo):
    parrafo = parrafo.lower()
    conteo = {}
    for caracter in parrafo:
        if caracter.isalpha():
            conteo[caracter] = conteo.get(caracter, 0) + 1
    return conteo

# Interfaz de usuario
st.title("Contador de letras en un párrafo")

parrafo = st.text_area("Introduce un párrafo:", height=200)

opcion = st.radio("¿Qué deseas hacer?", ["Contar una letra específica", "Contar todas las letras"])

if opcion == "Contar una letra específica":
    letra = st.text_input("Introduce la letra que deseas contar:", max_chars=1)
    if letra:
        if len(letra) != 1 or not letra.isalpha():
            st.error("Por favor, introduce solo una letra válida.")
        else:
            cantidad = contar_letra(parrafo, letra)
            st.success(f"La letra '{letra}' aparece {cantidad} veces en el párrafo.")
elif opcion == "Contar todas las letras":
    if st.button("Contar letras"):
        conteo = contar_todas_las_letras(parrafo)
        st.subheader("Conteo de todas las letras:")
        for letra in sorted(conteo.keys()):
            st.write(f"{letra}: {conteo[letra]}")
