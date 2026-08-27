import ollama

print("=" * 50)
print("TEXT GENERATION USING OLLAMA")
print("=" * 50)

prompt = input("\nEnter a prompt: ")

try:

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    print("\nGenerated Text:")
    print(response["response"])

except Exception as e:

    print("\nError connecting to Ollama:")
    print(e)
