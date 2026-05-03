


from sentence_transformers import SentenceTransformer, util 

# 1. Load a pre-trained "Mind" (Model)
model = SentenceTransformer('all-MiniLM-L6-v2')

#2. The Griots Strings
strings = [
    "A story about a young girl discovering her roots in a vibrant African village.",
    "A historical accoun of melanated inventors and their impact on modern technology.",
    "A guide on how to fix a broken car engine with simple tools."
]

# 3. Vectorization (Turning sentences into numbers)
embeddings = model.encode(strings)

# 4. The AI Calculation (Cosine Similarity)
# Comparing String A to B, and A to C 
sim_A_B = util.cos_sim(embeddings[0], embeddings[1])
sim_A_C = util.cos_sim(embeddings[0], embeddings[2])

print(f"Similarity between A and B: {sim_A_B.item():.4f}")
print(f"Similarity between A and C: {sim_A_C.item():.4f}")

