Aquí tienes una guía completa para crear una **página web en Streamlit** que:

* Explica cómo funcionan `while`, `for` e `if` en Python.
* Genera 10 preguntas con alternativas.
* Evalúa las respuestas y muestra el puntaje.
* Despliega globos si aciertas las 10 preguntas.

---

## ✅ Paso 1: Crea el repositorio en GitHub

1. Ve a [GitHub](https://github.com).
2. Crea un nuevo repositorio, por ejemplo: `python-condicionales-streamlit`.
3. Añade un archivo llamado `app.py`.

---

## ✅ Paso 2: Código de la aplicación Streamlit (`app.py`)

Copia este código y pégalo en el archivo `app.py` de tu repositorio:

````python
import streamlit as st
import random

st.set_page_config(page_title="Aprende Python - Condicionales y Bucles", page_icon="🐍")

st.title("🐍 Aprende Python: Condicionales y Bucles")

# Explicación teórica
with st.expander("📘 ¿Cómo funcionan 'if', 'for' y 'while' en Python?"):
    st.markdown("""
### 🔹 Condicional `if`
Se usa para ejecutar código solo si se cumple una condición.

```python
x = 10
if x > 5:
    print("x es mayor que 5")
````

### 🔹 Bucle `for`

Sirve para iterar sobre una secuencia (lista, cadena, etc.).

```python
for i in range(3):
    print(i)
```

### 🔹 Bucle `while`

Ejecuta un bloque de código mientras se cumpla una condición.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

```
""")
```

# Preguntas y respuestas

questions = \[
{
"question": "¿Qué palabra clave se usa para una estructura condicional en Python?",
"options": \["for", "if", "while"],
"answer": "if"
},
{
"question": "¿Cuál es la salida de este código?\n\nx = 3\nif x < 5:\n    print('menor')",
"options": \["mayor", "menor", "igual"],
"answer": "menor"
},
{
"question": "¿Qué estructura repite mientras una condición sea verdadera?",
"options": \["if", "while", "else"],
"answer": "while"
},
{
"question": "¿Qué función se usa comúnmente con 'for' para iterar un número de veces?",
"options": \["loop()", "range()", "repeat()"],
"answer": "range()"
},
{
"question": "¿Cuál es la salida de este código?\n\nfor i in range(2):\n    print(i)",
"options": \["1 2", "0 1", "0 1 2"],
"answer": "0 1"
},
{
"question": "¿Cuál es la condición para que este bucle termine?\n\nwhile x < 3:",
"options": \["x = 3", "x > 3", "x < 3"],
"answer": "x >= 3"
},
{
"question": "¿Qué palabra se usa para ejecutar una acción si la condición no se cumple?",
"options": \["elif", "else", "continue"],
"answer": "else"
},
{
"question": "¿Qué palabra permite evaluar múltiples condiciones?",
"options": \["elif", "else", "loop"],
"answer": "elif"
},
{
"question": "¿Qué imprime este código?\n\nx = 0\nwhile x < 2:\n    print(x)\n    x += 1",
"options": \["0 1", "1 2", "2 3"],
"answer": "0 1"
},
{
"question": "¿Qué hace el siguiente código?\n\nfor letra in 'hi':\n    print(letra)",
"options": \["h", "i", "h i"],
"answer": "h i"
},
]

random.shuffle(questions)

user\_answers = \[]
st.subheader("🧠 Quiz interactivo: 10 preguntas sobre Python")
for i, q in enumerate(questions):
user\_answer = st.radio(f"{i+1}. {q\['question']}", q\['options'], key=i)
user\_answers.append(user\_answer)

# Botón para enviar

if st.button("✅ Enviar respuestas"):
correct = 0
for i, q in enumerate(questions):
if user\_answers\[i] == q\["answer"]:
correct += 1

```
st.subheader(f"🎯 Tu puntaje: {correct} / 10")

if correct == 10:
    st.balloons()
    st.success("¡Perfecto! Has respondido todas las preguntas correctamente.")
elif correct >= 7:
    st.info("¡Muy bien! Pero puedes mejorar aún más.")
else:
    st.warning("Sigue practicando para mejorar tus conocimientos.")
```

```

---

## ✅ Paso 3: Publicar la app con Streamlit Cloud

1. Ve a [Streamlit Cloud](https://streamlit.io/cloud).
2. Inicia sesión con tu cuenta de GitHub.
3. Haz clic en **"New app"**.
4. Elige el repositorio (`python-condicionales-streamlit`) y el archivo `app.py`.
5. Presiona **"Deploy"**.

¡Tu app estará en línea en unos segundos!

---

## 🎁 Resultado Final

Una web didáctica en Streamlit que:
- Enseña estructuras `if`, `for`, `while`.
- Te permite autoevaluarte con preguntas aleatorias.
- Celebra tu perfección con 🎈 globos.

---

¿Quieres que genere también el `README.md` para tu repositorio de GitHub?
```
