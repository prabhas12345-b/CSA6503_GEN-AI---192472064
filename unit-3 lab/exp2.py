import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection("genai")

texts = [
    "Artificial intelligence enables machines to learn.",
    "Machine learning is a subset of artificial intelligence.",
    "Deep learning uses neural networks.",
    "Natural language processing deals with human language.",
    "Computer vision helps computers understand images."
]

embeddings = model.encode(texts).tolist()

collection.add(
    ids=[str(i) for i in range(len(texts))],
    documents=texts,
    embeddings=embeddings
)

query = "What is machine learning?"
q = model.encode([query]).tolist()

result = collection.query(
    query_embeddings=q,
    n_results=2
)

print("Query:", query)
print("\nSimilar Documents:")

for doc in result["documents"][0]:
    print("-", doc)