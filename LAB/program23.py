import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download sentence tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')

# Input text
text = """
Natural language processing is a branch of artificial intelligence.
It helps computers understand human language.
NLP is used in chatbots, translation, and text analysis.
These applications make communication with computers easier.
"""

# Split text into sentences
sentences = nltk.sent_tokenize(text)

print("Input Text:")
print(text)

print("\nSentences:")
for i, sentence in enumerate(sentences, 1):
    print(f"{i}. {sentence}")

# Convert sentences into TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Calculate similarity between consecutive sentences
similarities = []

for i in range(len(sentences) - 1):
    similarity = cosine_similarity(
        tfidf_matrix[i:i + 1],
        tfidf_matrix[i + 1:i + 2]
    )[0][0]

    similarities.append(similarity)

    print(
        f"\nSimilarity between Sentence {i} "
        f"and Sentence {i + 1}: {similarity:.4f}"
    )

# Calculate average coherence score
if similarities:
    coherence_score = sum(similarities) / len(similarities)
else:
    coherence_score = 0

print(f"\nCoherence Score: {coherence_score:.4f}")

# Interpret the score
if coherence_score >= 0.20:
    print("Coherence Level: HIGH")
elif coherence_score >= 0.10:
    print("Coherence Level: MEDIUM")
else:
    print("Coherence Level: LOW")