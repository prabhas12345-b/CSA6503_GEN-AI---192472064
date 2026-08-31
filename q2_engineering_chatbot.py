from transformers import pipeline

print("Loading Engineering AI Chatbot...")
chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("\n==========================================")
print("      ENGINEERING SUPPORT CHATBOT")
print("==========================================")
print("Type 'exit' to stop.\n")

while True:
    question = input("Engineer: ")

    if question.lower() == "exit":
        print("AI: Thank you!")
        break

    prompt = f"""You are an engineering support assistant.
Provide a clear technical explanation and solution.

Question: {question}

Answer:"""

    result = chatbot(
        prompt,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.7
    )

    answer = result[0]["generated_text"]

    print("\nAI:", answer)
    print()