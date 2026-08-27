import ollama

print("=" * 50)
print("LOCAL LLM QUESTION ANSWERING SYSTEM")
print("=" * 50)

print("\nEnter your question.")
print("Type 'exit' to stop the program.\n")

while True:

    question = input("Question: ")

    if question.lower() == "exit":
        print("\nProgram ended.")
        break

    if not question.strip():
        print("Please enter a question.\n")
        continue

    prompt = f"""
You are a helpful question-answering assistant.

Answer the following question clearly and simply.

Question:
{question}

Give a direct and useful answer.
"""

    try:

        response = ollama.generate(
            model="llama3.2",
            prompt=prompt
        )

        print("\nAnswer:")
        print(response["response"])
        print()

    except Exception as e:

        print("\nError connecting to Ollama:")
        print(e)
        print()
