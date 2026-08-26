from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load English-to-French translation model
model_name = "Helsinki-NLP/opus-mt-en-fr"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# English text
text = "Natural Language Processing is an important field of Artificial Intelligence."

# Tokenize input
inputs = tokenizer(text, return_tensors="pt")

# Generate French translation
outputs = model.generate(
    **inputs,
    max_new_tokens=100
)

# Decode translation
translation = tokenizer.decode(
    outputs[0],
    skip_special_tokens=True
)

# Display result
print("English Text:")
print(text)

print("\nFrench Translation:")
print(translation)