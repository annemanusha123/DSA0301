from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Collection of documents
documents = [
    "Natural language processing is a branch of artificial intelligence.",
    "Machine learning is used in artificial intelligence.",
    "Natural language processing helps computers understand human language.",
    "Python is a popular programming language for machine learning."
]

# User query
query = "natural language processing"

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert documents and query into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

# Calculate cosine similarity
similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()

# Rank documents according to similarity
ranked_documents = similarity_scores.argsort()[::-1]

print("Query:")
print(query)

print("\nDocument Ranking:")

for rank, index in enumerate(ranked_documents, start=1):
    print(
        f"Rank {rank}: Document {index + 1} "
        f"(Similarity = {similarity_scores[index]:.4f})"
    )
    print("Text:", documents[index])
    print()