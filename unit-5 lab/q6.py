import ollama

print("=" * 50)
print("QUESTION ANSWERING USING OLLAMA")
print("=" * 50)

question = input("\nEnter your question: ")

prompt = f"""
Answer the following question clearly and accurately.

Question:
{question}

Give a simple answer suitable for an engineering student.
"""

try:

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    print("\nAnswer:")
    print(response["response"])

except Exception as e:

    print("\nError:")
    print(e)
