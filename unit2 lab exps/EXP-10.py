from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

schema = """
Table: Student
student_id
name
department
marks
"""

requirement = input("Enter SQL Requirement: ")

prompt = f"""
You are an SQL Expert.

Database Schema:
{schema}

Requirement:
{requirement}

Generate only SQL query.
"""

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print("\nGenerated SQL Query:\n")
print(response.output_text)
