def pluralize(word):
    # State 0: Check the ending of the word

    # Words ending in s, x, z, ch, or sh
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    # Consonant + y
    elif word.endswith("y") and len(word) > 1 and word[-2] not in "aeiou":
        return word[:-1] + "ies"

    # Default rule
    else:
        return word + "s"


words = [
    "cat",
    "dog",
    "bus",
    "box",
    "church",
    "brush",
    "baby",
    "toy"
]

print("FINITE-STATE MORPHOLOGICAL PARSER")
print("-" * 40)

for word in words:
    plural = pluralize(word)
    print(word, "->", plural)