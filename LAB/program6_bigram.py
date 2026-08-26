from collections import defaultdict
import random

# Training text
text = """
natural language processing is a field of artificial intelligence
natural language processing helps computers understand human language
machine learning is used in natural language processing
natural language processing is useful for chatbots
"""

# Convert text into words
words = text.lower().split()

# Create Bigram Model
bigram_model = defaultdict(list)

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]

    bigram_model[current_word].append(next_word)


# Generate text
def generate_text(start_word, length=15):
    current_word = start_word
    generated_words = [current_word]

    for _ in range(length - 1):

        next_words = bigram_model.get(current_word)

        if not next_words:
            break

        current_word = random.choice(next_words)
        generated_words.append(current_word)

    return " ".join(generated_words)


print("BIGRAM N-GRAM TEXT GENERATION")
print("-" * 40)

start_word = "natural"

generated_text = generate_text(start_word, 15)

print("Generated Text:")
print(generated_text)