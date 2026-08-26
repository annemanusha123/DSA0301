# Simple Top-Down Parser for Context-Free Grammar

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

sentence = "the cat chased a dog".split()


def parse(symbol, words, position):
    # Terminal symbol
    if symbol not in grammar:
        if position < len(words) and symbol == words[position]:
            return position + 1
        return None

    # Try each production rule
    for rule in grammar[symbol]:
        current_position = position
        success = True

        for part in rule:
            result = parse(part, words, current_position)

            if result is None:
                success = False
                break

            current_position = result

        if success:
            return current_position

    return None


print("Sentence:", " ".join(sentence))
print("\nGrammar:")
print("S -> NP VP")
print("NP -> Det N")
print("VP -> V NP")
print("Det -> the | a")
print("N -> cat | dog")
print("V -> chased | saw")

result = parse("S", sentence, 0)

print("\nParsing Result:")

if result == len(sentence):
    print("Sentence accepted by the grammar.")
else:
    print("Sentence rejected by the grammar.")