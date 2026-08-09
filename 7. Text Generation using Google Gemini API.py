import google.generativeai as genai

# Replace with your Gemini API Key
genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = input("Enter your prompt: ")

response = model.generate_content(prompt)

print("\nGenerated Response:\n")
print(response.text)