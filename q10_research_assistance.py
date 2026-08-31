from transformers import pipeline

print("Loading Research Assistant...")

research_ai = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)

print("\n==========================================")
print("         AI RESEARCH ASSISTANT")
print("==========================================")

topic = input(
    "\nEnter research topic: "
)

prompt = f"""
You are an academic research assistant.

Research Topic:
{topic}

Provide:

1. Introduction
2. Important keywords
3. Relevant research areas
4. Applications
5. Advantages
6. Challenges
7. A concise summary

Keep the explanation simple and suitable for an engineering student.
"""

print("\nGenerating research information...\n")

result = research_ai(
    prompt,
    max_new_tokens=500,
    do_sample=True,
    temperature=0.7
)

answer = result[0]["generated_text"]

print("==========================================")
print("        RESEARCH INFORMATION")
print("==========================================")
print(answer)