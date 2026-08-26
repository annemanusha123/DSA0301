import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download('wordnet')
nltk.download('omw-1.4')

# Word to explore
word = "bank"

# Retrieve synsets
synsets = wordnet.synsets(word)

print("Word:", word)

print("\nNumber of Synsets:", len(synsets))

print("\nSynsets and Meanings:")

for synset in synsets[:5]:
    print("\nSynset:", synset.name())
    print("Definition:", synset.definition())
    print("Examples:", synset.examples())

# Display synonyms
print("\nSynonyms:")

synonyms = set()

for synset in synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print(", ".join(sorted(synonyms)))