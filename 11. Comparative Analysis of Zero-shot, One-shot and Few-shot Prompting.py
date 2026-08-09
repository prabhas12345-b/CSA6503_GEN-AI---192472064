from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

task = "Write a Python function to check prime numbers."

prompts = {
    "Zero-shot": task,

    "One-shot": """
Example:
Input: Find factorial
Output:
def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

Task:
Write a Python function to check prime numbers.
""",

    "Few-shot": """
Example 1:
Input: Sum of numbers
Output:
def total(nums):
    return sum(nums)

Example 2:
Input: Maximum number
Output:
def maximum(nums):
    return max(nums)

Task:
Write a Python function to check prime numbers.
"""
}

for name, prompt in prompts.items():
    print("=" * 50)
    print(name)
    print("=" * 50)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    print(response.output_text)
    print()