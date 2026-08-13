from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma(
    persist_directory="rag_db",
    embedding_function=embeddings
)

retriever = db.as_retriever(search_kwargs={"k": 2})

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

print("GenAI Chatbot")
print("Type 'exit' to stop")

while True:
    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)
    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
Answer using only the following context.

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)

    print("Bot:", response.content)