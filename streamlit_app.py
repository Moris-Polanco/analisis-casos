import openai
import streamlit as st
import os

# Set up the OpenAI API client
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Añade un título a la aplicación
st.title("Analizador de casos de ética")
st.caption("Responde desde cuatro puntos de vista: deontológico (Kant), utilitarista (John Stuart Mill), de las virtudes (Aristóteles) y objetivista (Ayn Rand)")
st.caption("Por Moris Polanco")
# Añade un cuadro de texto de Streamlit para que el usuario pueda ingresar el caso de ética a analizar
caso = st.text_area("Ingresa el caso de ética a analizar:")

if st.button("Analizar"):
    # Escribe aquí el código que quieres que se ejecute al hacer clic en el botón "Analizar"
    modelo = "text-davinci-003"
    prompt = (f"Analiza el caso de ética siguiente desde la perspectiva de cuatro teorías: deontologismo (Kant), utilitarismo (John Stuart Mill), ética de las virtudes (Aristóteles) y objetivismo (Ayn Rand).\n\nCaso: {caso}"
              f"\n\nAnálisis desde la perspectiva de Kant:\n\nAnálisis desde la perspectiva de John Stuart Mill:\n\nAnálisis desde la perspectiva de Aristóteles:\n\nAnálisis desde la perspectiva de Ayn Rand:")

    completions = openai.Completion.create(engine=modelo, prompt=prompt, max_tokens=1024, n=1,stop=None,temperature=0.5)
    analisis = completions.choices[0].text


    # Divide el análisis en cuatro partes y muestra cada una en la aplicación de Streamlit
    partes = analisis.split("\n\n")
    st.markdown("# Análisis desde la perspectiva de Kant")
    st.markdown(partes[1])
    st.markdown("# Análisis desde la perspectiva de John Stuart Mill")
    st.markdown(partes[2])
    st.markdown("# Análisis desde la perspectiva de Aristóteles")
    st.markdown(partes[3])
    st.markdown("# Análisis desde la perspectiva de Ayn Rand")
    st.markdown(partes[4])
