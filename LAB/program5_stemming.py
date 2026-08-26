from nltk.stem import PorterStemmer

# Create Porter Stemmer object
stemmer = PorterStemmer()

# List of words
words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "connected",
    "connection",
    "running",
    "easily",
    "fairly"
]

print("PORTER STEMMER")
print("-" * 40)

for word in words:
    stemmed_word = stemmer.stem(word)
    print(word, "->", stemmed_word)