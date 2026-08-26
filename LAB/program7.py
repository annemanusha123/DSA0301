import nltk

from nltk import CFG
from nltk.parse import ChartParser

# Define a Context-Free Grammar
grammar = CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'saw'
""")

# Create a parser
parser = ChartParser(grammar)

# Input sentence
sentence = "the cat chased a dog".split()

# Generate parse tree
print("Sentence:", " ".join(sentence))
print("\nParse Tree:")

trees = list(parser.parse(sentence))

if trees:
    for tree in trees:
        print(tree)
        tree.pretty_print()
else:
    print("No parse tree found.")