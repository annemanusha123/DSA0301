import re

# Function to parse an FOPC expression
def parse_fopc(expression):

    expression = expression.strip()

    # Universal quantifier
    universal = re.match(
        r'^∀([a-zA-Z])\s+(.+)$',
        expression
    )

    if universal:
        variable = universal.group(1)
        formula = universal.group(2)

        print("Expression Type: Universal Quantifier")
        print("Variable:", variable)
        print("Formula:", formula)

        return

    # Existential quantifier
    existential = re.match(
        r'^∃([a-zA-Z])\s+(.+)$',
        expression
    )

    if existential:
        variable = existential.group(1)
        formula = existential.group(2)

        print("Expression Type: Existential Quantifier")
        print("Variable:", variable)
        print("Formula:", formula)

        return

    # Predicate with two arguments
    predicate_two = re.match(
        r'^([A-Za-z][A-Za-z0-9_]*)\(([^,]+),\s*([^)]+)\)$',
        expression
    )

    if predicate_two:
        predicate = predicate_two.group(1)
        arg1 = predicate_two.group(2).strip()
        arg2 = predicate_two.group(3).strip()

        print("Expression Type: Binary Predicate")
        print("Predicate:", predicate)
        print("Argument 1:", arg1)
        print("Argument 2:", arg2)

        return

    # Predicate with one argument
    predicate_one = re.match(
        r'^([A-Za-z][A-Za-z0-9_]*)\(([^)]+)\)$',
        expression
    )

    if predicate_one:
        predicate = predicate_one.group(1)
        argument = predicate_one.group(2).strip()

        print("Expression Type: Unary Predicate")
        print("Predicate:", predicate)
        print("Argument:", argument)

        return

    print("Invalid FOPC expression.")


# Test expressions
expressions = [
    "Student(Anu)",
    "Likes(Anu, AI)",
    "∀x Student(x)",
    "∃x Teacher(x)"
]

for expression in expressions:
    print("\nExpression:", expression)
    parse_fopc(expression)