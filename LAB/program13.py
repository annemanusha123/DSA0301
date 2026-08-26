import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define Context-Free Grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'saw'
""")

# Create parser
parser = ChartParser(grammar)

# Input sentence
sentence = "the cat chased a dog".split()

print("Sentence:")
print(" ".join(sentence))

print("\nParse Tree:")

# Generate parse tree
trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        print()
        tree.pretty_print()
else:
    print("No parse tree found.")