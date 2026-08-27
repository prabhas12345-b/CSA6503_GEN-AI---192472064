import ollama
import chromadb

print("=" * 60)
print("LOCAL RAG SYSTEM USING OLLAMA AND CHROMADB")
print("=" * 60)

# Read engineering document
with open("engineering.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split document into smaller chunks
chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="engineering_documents"
)

# Create embeddings and store documents
for i, chunk in enumerate(chunks):

    embedding_response = ollama.embed(
        model="nomic-embed-text",
        input=chunk
    )

    embedding = embedding_response["embeddings"][0]

    collection.upsert(
        ids=[str(i)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("\nEngineering document loaded into vector database.")

question = input("\nEnter your technical question: ")

# Create query embedding
query_response = ollama.embed(
    model="nomic-embed-text",
    input=question
)

query_embedding = query_response["embeddings"][0]

# Retrieve relevant documents
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

retrieved_documents = results["documents"][0]

context = "\n\n".join(retrieved_documents)

# Generate answer using retrieved context
prompt = f"""
You are an engineering assistant.

Answer the question using ONLY the provided context.

If the answer is not available in the context,
say that the information is not available.

CONTEXT:
{context}

QUESTION:
{question}

Give a clear and simple technical answer.
"""

response = ollama.generate(
    model="llama3.2",
    prompt=prompt
)

print("\nRetrieved Information:")
print(context)

print("\nGenerated Answer:")
print(response["response"])