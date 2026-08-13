from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [
    "Artificial intelligence is used in many applications.",
    "Machine learning is a part of artificial intelligence.",
    "I like playing cricket."
]

query = "Applications of artificial intelligence"

embeddings = model.encode(texts)
q = model.encode(query)

scores = model.similarity(q, embeddings)[0]

for text, score in zip(texts, scores):
    print(round(float(score), 4), "-", text)