import ollama

print("=" * 60)
print("HALLUCINATION ANALYSIS USING LOCAL LLM")
print("=" * 60)

reference = """
College Technical Lab Reference:

The Engineering AI Lab was established in 2024.
The laboratory contains 30 computers.
The lab uses Python and Ollama for local AI experiments.
The lab is located in Block B.
"""

question = input("\nAsk a question about the reference: ")

prompt = f"""
Answer the question using the reference information below.

REFERENCE:
{reference}

QUESTION:
{question}

If the answer is not present in the reference,
clearly say that the information is not available.
Do not invent facts.
"""

try:

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    print("\nLLM Response:")
    print(response["response"])

    print("\nReference Information:")
    print(reference)

except Exception as e:

    print("\nError:")
    print(e)