


import chromadb
from chromadb.utils import embedding_functions

# 1. Initialize the "Librarian" (ChromaDB Client)
# This creates a local database in your project folder
client = chromadb.Client()

# 2. Set up the "Mind" (Embedding Function)
# Chroma uses the same sentence-transformers model under the hood
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

# 3. Create a "Collection" (The actual bookshelf)
collection = client.create_collection(name="mml_principles", embedding_function=sentence_transformer_ef)

# 4. The Data: MML Principles 
mml_knowledge = [
    "David Blackwell was the first African American inducted into the National Academy of Sciences.",
    "The Information Bottleneck is a principle where we reduce noise to find the core signal.",
    "Inference Engineering is the practice of using AI to make decisions under uncertainty.",
    "Blackwell's Theorem relates to comparing experiments and decision-making risks.",
    "Melanated Machine Learning (MML) bridges cultural intuition with technical mastery."
]

# 5. Add knowledge to the Collection
collection.add(
    documents=mml_knowledge,
    ids=[f"id{i}" for i in range(len(mml_knowledge))]
)

# 6. The Query Function with Thresholding 
def ask_mml(query_text):
    results = collection.query(
        query_texts=[query_text],
        n_results=1
    )
    
    # Chroma returns 'distances' . 0.0 is a perfect match.
    # For this model, anything over 1.0 - 1.2 is usually "too far."
    distance = results['distances'][0][0]
    document = results['documents'][0][0]

    threshold = 1.1
    if distance > threshold: 
        return f"OUT OF BOUNDS: I am not certain enough to answer. (Distance: {distance:.4f})"
    else:
        return f"MATCH FOUND (Distance: {distance:.4f}): {document}"
    
# --- TEST RUNS ---
print("--- TEST 1 ---")
print(ask_mml("Who is the mathematician?"))

print("\n--- TEST 2 ---")
print(ask_mml("Tell me about noise and signal."))

print("\n--- TEST 3 ---")
print(ask_mml("How do I bake a chocolate cake?"))  # This should trigger the threshold 

