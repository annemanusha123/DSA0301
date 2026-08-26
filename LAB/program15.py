import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

# Define a Probabilistic Context-Free Grammar
grammar = PCFG.fromstring("""
    S -> NP VP [1.0]

    NP -> Det N [0.6]
    NP -> Det Adj N [0.4]

    VP -> V NP [1.0]

    Det -> 'the' [0.5]
    Det -> 'a' [0.5]

    Adj -> 'small' [0.5]
    Adj -> 'big' [0.5]

    N -> 'cat' [0.5]
    N -> 'dog' [0.5]

    V -> 'chased' [0.5]
    V -> 'saw' [0.5]
""")

# Create Viterbi parser
parser = ViterbiParser(grammar)

# Input sentence
sentence = "the small cat chased a dog".split()

print("Sentence:")
print(" ".join(sentence))

print("\nPCFG Parse Tree:")

# Parse the sentence
try:
    trees = list(parser.parse(sentence))

    if trees:
        for tree in trees:
            print(tree)
            print("\nProbability:", tree.prob())
            tree.pretty_print()
    else:
        print("No parse found.")

except ValueError:
    print("The sentence cannot be parsed by the grammar.")