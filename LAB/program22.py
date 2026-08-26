import nltk

# Download required resources
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

# Input text
text = "Ravi went to the library. He borrowed a book. It was very interesting."

# Split text into sentences
sentences = nltk.sent_tokenize(text)

# Pronouns to resolve
pronouns = {
    "he": "male person",
    "she": "female person",
    "it": "object or thing",
    "they": "plural noun"
}

# Store previously mentioned nouns
previous_nouns = []

print("Input Text:")
print(text)

print("\nReference Resolution:")

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)

    for word, tag in tags:

        # Check for pronouns
        if word.lower() in pronouns:

            if previous_nouns:
                reference = previous_nouns[-1]
                print(f"{word} -> {reference}")

        # Store proper nouns and common nouns
        elif tag.startswith("NN"):
            previous_nouns.append(word)
