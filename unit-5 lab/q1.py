import streamlit as st
import ollama

st.title("Local LLM Text Generation")

st.write("Generate text using a locally running Large Language Model.")

prompt = st.text_area(
    "Enter your prompt:",
    "Explain Artificial Intelligence in simple words."
)

if st.button("Generate Text"):

    if prompt.strip():

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        st.subheader("Generated Text")

        st.write(response["message"]["content"])

    else:
        st.warning("Please enter a prompt.")    
