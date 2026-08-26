import nltk
from nltk import RegexpTagger

# Download tokenizer
nltk.download('punkt')
nltk.download('punkt_tab')

# Input sentence
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenize the sentence
words = nltk.word_tokenize(sentence)

# Define regular expression rules
patterns = [
    (r'.*ing$', 'VBG'),       # Words ending with -ing
    (r'.*ed$', 'VBD'),        # Words ending with -ed
    (r'.*es$', 'VBZ'),        # Words ending with -es
    (r'.*s$', 'NNS'),         # Words ending with -s
    (r'.*ly$', 'RB'),         # Adverbs ending with -ly
    (r'.*ous$', 'JJ'),        # Adjectives ending with -ous
    (r'.*', 'NN')             # Default: noun
]

# Create rule-based tagger
tagger = RegexpTagger(patterns)

# Perform POS tagging
tagged_words = tagger.tag(words)

# Display output
print("Input Sentence:")
print(sentence)

print("\nRule-Based POS Tags:")
for word, tag in tagged_words:
    print(word, "->", tag)