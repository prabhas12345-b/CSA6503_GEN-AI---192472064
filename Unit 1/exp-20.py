from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompts = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science"
]
for p in prompts:
    print("\nPrompt:", p)
    output = generator(p, max_length=40)
    print(output[0]["generated_text"])