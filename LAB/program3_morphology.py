import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

# Create stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

words = [
    "playing",
    "played",
    "plays",
    "studies",
    "studying",
    "cars",
    "running"
]

print("MORPHOLOGICAL ANALYSIS")
print("-" * 40)

for word in words:
    stem = stemmer.stem(word)
    lemma = lemmatizer.lemmatize(word)

    print("Word   :", word)
    print("Stem   :", stem)
    print("Lemma  :", lemma)
    print()