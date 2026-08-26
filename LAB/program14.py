import nltk
from nltk import CFG
from nltk.parse import ChartParser

# Define a CFG with subject-verb agreement
grammar = CFG.fromstring("""
    S -> NP_S VP_S
    S -> NP_P VP_P

    NP_S -> Det_S N_S
    NP_P -> Det_P N_P

    VP_S -> V_S
    VP_P -> V_P

    Det_S -> 'the'
    Det_P -> 'the'

    N_S -> 'boy' | 'girl'
    N_P -> 'boys' | 'girls'

    V_S -> 'runs' | 'plays'
    V_P -> 'run' | 'play'
""")

# Create parser
parser = ChartParser(grammar)


# Function to check agreement
def check_agreement(sentence):
    words = sentence.lower().split()

    trees = list(parser.parse(words))

    print("Sentence:", sentence)

    if trees:
        print("Agreement: CORRECT")
    else:
        print("Agreement: INCORRECT")


# Test sentences
print("=== Subject-Verb Agreement Checking ===\n")

check_agreement("the boy runs")

print()

check_agreement("the boys run")

print()

check_agreement("the boy run")

print()

check_agreement("the girls plays")