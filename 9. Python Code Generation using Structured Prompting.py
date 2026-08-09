from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

problem = input("Enter Python problem: ")

structured_prompt = f"""
You are a Python programming expert.

Task:
Generate only Python code.

Requirements:
1. Use Python 3.
2. Add comments.
3. Use functions if needed.

Problem:
{problem}
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=structured_prompt
)

print("\nGenerated Python Code:\n")
print(response.output_text)