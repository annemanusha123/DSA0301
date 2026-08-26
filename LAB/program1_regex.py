import re

text = "Natural Language Processing is interesting. NLP is used in AI."

# Search for the word "NLP"
match = re.search(r"\bNLP\b", text)

if match:
    print("Pattern found:", match.group())
    print("Position:", match.start())
else:
    print("Pattern not found")

# Find all words starting with "N"
words = re.findall(r"\bN\w*", text)

print("Words starting with N:", words)

# Replace NLP with Natural Language Processing
new_text = re.sub(r"\bNLP\b", "Natural Language Processing", text)

print("After replacement:")
print(new_text)