from transformers import pipeline

# Load a text generation model
generator = pipeline(
    "text-generation",
    model="distilgpt2"
)

# Given prompt
prompt = "Natural Language Processing is"

# Generate text
result = generator(
    prompt,
    max_new_tokens=50,
    num_return_sequences=1
)

# Display output
print("Prompt:")
print(prompt)

print("\nGenerated Text:")
print(result[0]["generated_text"])