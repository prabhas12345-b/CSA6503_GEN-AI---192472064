from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

text = open("documents/genai.txt", encoding="utf-8").read()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = splitter.create_documents([text])

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="rag_db"
)

retriever = db.as_retriever(search_kwargs={"k": 2})

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

question = input("Ask a question: ")

docs = retriever.invoke(question)
context = "\n".join(d.page_content for d in docs)

prompt = f"""
Answer using only the following context.

Context:
{context}

Question:
{question}
"""

answer = llm.invoke(prompt)

print("\nAnswer:")
print(answer.content)