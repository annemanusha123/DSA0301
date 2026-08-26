import nltk
from nltk.tag import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

# Input sentence
sentence = "The dog runs quickly."

# Tokenize
words = nltk.word_tokenize(sentence)

# Initial tagging using simple rules
patterns = [
    (r'.*ly$', 'NN'),
    (r'.*s$', 'NN'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)
initial_tags = tagger.tag(words)

print("Initial Tags:")
for word, tag in initial_tags:
    print(word, "->", tag)

# Transformation rules
transformed_tags = []

for word, tag in initial_tags:

    # Rule 1: Words ending in 'ly' are adverbs
    if word.lower().endswith("ly"):
        tag = "RB"

    # Rule 2: 'runs' is a singular verb
    elif word.lower() == "runs":
        tag = "VBZ"

    # Rule 3: 'dog' is a noun
    elif word.lower() == "dog":
        tag = "NN"

    # Rule 4: 'the' is a determiner
    elif word.lower() == "the":
        tag = "DT"

    transformed_tags.append((word, tag))

print("\nAfter Transformation Rules:")
for word, tag in transformed_tags:
    print(word, "->", tag)