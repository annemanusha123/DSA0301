import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet

# Download required NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input sentence
sentence = "The intelligent student reads a book."

# Tokenize and POS tag
words = word_tokenize(sentence)
tags = pos_tag(words)

# Extract simple noun phrases
noun_phrases = []

for i in range(len(tags)):
    word, tag = tags[i]

    # Adjective + noun
    if tag.startswith("JJ") and i + 1 < len(tags):
        next_word, next_tag = tags[i + 1]

        if next_tag.startswith("NN"):
            noun_phrases.append(word + " " + next_word)

    # Noun
    elif tag.startswith("NN"):
        if i == 0 or not tags[i - 1][1].startswith("JJ"):
            noun_phrases.append(word)

print("Sentence:")
print(sentence)

print("\nNoun Phrases and Meanings:")

for phrase in noun_phrases:
    # Use the main noun for WordNet lookup
    main_word = phrase.split()[-1]

    synsets = wordnet.synsets(main_word)

    print("\nNoun Phrase:", phrase)

    if synsets:
        print("Meaning:", synsets[0].definition())
    else:
        print("Meaning: Not found in WordNet")