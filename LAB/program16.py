import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Sundar Pichai is the CEO of Google. He lives in California."

# Process the text
doc = nlp(text)

# Display the input text
print("Input Text:")
print(text)

# Display named entities
print("\nNamed Entities:")

for entity in doc.ents:
    print(entity.text, "->", entity.label_)