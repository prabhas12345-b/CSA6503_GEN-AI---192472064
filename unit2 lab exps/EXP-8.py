from huggingface_hub import InferenceClient

# Replace with your Hugging Face API Token
client = InferenceClient(
    provider="hf-inference",
    api_key="YOUR_HF_API_TOKEN",
)

prompt = input("Enter your prompt: ")

response = client.text_generation(
    prompt,
    model="gpt2",
    max_new_tokens=100
)

print("\nGenerated Response:\n")
print(response)
