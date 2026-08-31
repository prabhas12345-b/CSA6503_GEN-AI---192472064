from transformers import pipeline

print("Loading AI model...")
print("Please wait...")

chatbot = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("\n==========================================")
print("   ENGINEERING COLLEGE AI CHATBOT")
print("==========================================")
print("Type 'exit' to stop the chatbot.\n")

while True:
    question = input("Student: ")

    if question.lower() == "exit":
        print("Chatbot: Thank you! Goodbye.")
        break

    messages = [
        {
            "role": "system",
            "content": "You are an AI assistant for an engineering college. Answer student questions clearly and simply."
        },
        {
            "role": "user",
            "content": question
        }
    ]

    result = chatbot(
        messages,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    answer = result[0]["generated_text"][-1]["content"]

    print("Chatbot:", answer)
    print()