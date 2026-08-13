from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import ChatOllama

loader = PyPDFLoader("documents/ai_notes.pdf")
docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_documents(docs)

embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)

db = Chroma.from_documents(
    chunks,
    embeddings,
    persist_directory="pdf_db"
)

retriever = db.as_retriever(search_kwargs={"k": 3})

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

print("AI Document Assistant")
print("Type 'exit' to stop")

while True:
    question = input("\nQuestion: ")

    if question.lower() == "exit":
        break

    docs = retriever.invoke(question)
    context = "\n".join(d.page_content for d in docs)

    prompt = f"""
Answer using only the document context.

Context:
{context}

Question:
{question}

If the answer is not in the document, say:
Information not found in the document.
"""

    answer = llm.invoke(prompt)

    print("\nAnswer:", answer.content)