import nltk
from nltk.wsd import lesk

# Download required WordNet resources
nltk.download('wordnet')
nltk.download('omw-1.4')

# Sentence containing an ambiguous word
sentence = "I went to the bank to deposit money."

# Tokenize the sentence
words = sentence.split()

# Apply Lesk algorithm to the word "bank"
sense = lesk(words, "bank")

# Display the results
print("Sentence:")
print(sentence)

print("\nAmbiguous Word:")
print("bank")

print("\nDisambiguated Sense:")

if sense:
    print("Synset:", sense.name())
    print("Definition:", sense.definition())
    print("Examples:", sense.examples())
else:
    print("No sense found.")