import streamlit as st
import ollama

st.set_page_config(
    page_title="Local LLM Text Summarization",
    page_icon="📝"
)

st.title("📝 Local LLM Text Summarization")

st.write(
    "Summarize text using a locally running Large Language Model with Ollama."
)

text = st.text_area(
    "Enter the text to summarize:",
    height=250,
    placeholder="Enter a paragraph or article here..."
)

if st.button("Summarize Text"):

    if not text.strip():
        st.warning("Please enter some text.")

    else:

        prompt = f"""
Summarize the following text in simple and clear language.
Keep the summary short and include the important points.

Text:
{text}
"""

        with st.spinner("Generating summary..."):

            try:

                response = ollama.generate(
                    model="llama3.2",
                    prompt=prompt
                )

                st.subheader("Summary")

                st.write(response["response"])

            except Exception as e:

                st.error("Unable to connect to Ollama.")

                st.write("Error details:")

                st.code(str(e))