import ollama
import chromadb

print("=" * 65)
print("ENGINEERING TROUBLESHOOTING RAG SYSTEM")
print("=" * 65)

# Read troubleshooting document
with open("troubleshooting.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Split into sections
chunks = [
    chunk.strip()
    for chunk in text.split("\n\n")
    if chunk.strip()
]

# Create vector database
client = chromadb.PersistentClient(
    path="./troubleshooting_db"
)

collection = client.get_or_create_collection(
    name="troubleshooting_documents"
)

# Store document embeddings
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

print("\nTroubleshooting documents loaded.")

problem = input(
    "\nDescribe your engineering problem: "
)

# Embed user problem
query_response = ollama.embed(
    model="nomic-embed-text",
    input=problem
)

query_embedding = query_response["embeddings"][0]

# Retrieve relevant troubleshooting information
results = collection.query(
    query_embeddings=[query_embedding],
    n_results=2
)

retrieved_documents = results["documents"][0]

context = "\n\n".join(retrieved_documents)

# Generate troubleshooting recommendations
prompt = f"""
You are an engineering troubleshooting assistant.

Use ONLY the troubleshooting information provided below.

Provide:
1. Identified problem
2. Step-by-step troubleshooting recommendations
3. A final recommendation

Do not invent technical procedures that are not supported
by the provided information.

TROUBLESHOOTING INFORMATION:
{context}

USER PROBLEM:
{problem}
"""

response = ollama.generate(
    model="llama3.2",
    prompt=prompt
)

print("\nRetrieved Information:")
print(context)

print("\nStep-by-Step Recommendation:")
print(response["response"])
