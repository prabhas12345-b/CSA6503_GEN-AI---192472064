import ollama

print("=" * 55)
print("LOCAL LLM TRANSLATION AND PARAPHRASING")
print("=" * 55)

print("\n1. Translation")
print("2. Paraphrasing")

choice = input("\nEnter your choice (1 or 2): ")

text = input("\nEnter the text: ")

if choice == "1":

    language = input("Enter target language: ")

    prompt = f"""
Translate the following text into {language}.
Give only the translated text.

Text:
{text}
"""

elif choice == "2":

    prompt = f"""
Paraphrase the following text using simple and clear words.
Keep the original meaning.

Text:
{text}
"""

else:

    print("Invalid choice.")
    exit()

try:

    response = ollama.generate(
        model="llama3.2",
        prompt=prompt
    )

    print("\nResult:")
    print(response["response"])

except Exception as e:

    print("\nError:")
    print(e)
