from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

prompts = [
    "Explain Artificial Intelligence.",

    "Explain Artificial Intelligence in simple language for school students.",

    """Explain Artificial Intelligence.
Include:
1. Definition
2. Applications
3. Advantages
4. Conclusion
Limit to 200 words."""
]

for i, prompt in enumerate(prompts, start=1):
    print("=" * 50)
    print(f"Prompt {i}")
    print("=" * 50)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print(response.output_text)
    print()