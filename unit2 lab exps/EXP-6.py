import google.generativeai as genai
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-2.5-flash")
prompt = input("Enter your prompt: ")
response = model.generate_content(prompt)
print("\nGenerated Text:\n")
print(response.text)
