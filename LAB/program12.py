# Simple Earley Parser for Context-Free Grammar

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["cat"], ["dog"]],
    "V": [["chased"], ["saw"]]
}

sentence = "the cat chased a dog".split()


def earley_parser(words):
    n = len(words)

    # Chart contains states for each word position
    chart = [[] for _ in range(n + 1)]

    # State format:
    # (left side, right side, dot position, origin)
    chart[0].append(("S'", ["S"], 0, 0))

    for i in range(n + 1):
        changed = True

        while changed:
            changed = False

            for state in chart[i].copy():
                lhs, rhs, dot, origin = state

                # COMPLETER
                if dot == len(rhs):
                    for previous in chart[origin].copy():
                        plhs, prhs, pdot, porigin = previous

                        if pdot < len(prhs) and prhs[pdot] == lhs:
                            new_state = (
                                plhs,
                                prhs,
                                pdot + 1,
                                porigin
                            )

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

                # PREDICTOR
                elif rhs[dot] in grammar:
                    next_symbol = rhs[dot]

                    for production in grammar[next_symbol]:
                        new_state = (
                            next_symbol,
                            production,
                            0,
                            i
                        )

                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                            changed = True

                # SCANNER
                elif i < n and rhs[dot] == words[i]:
                    new_state = (
                        lhs,
                        rhs,
                        dot + 1,
                        origin
                    )

                    if new_state not in chart[i + 1]:
                        chart[i + 1].append(new_state)

    # Check accepting state
    accepting_state = ("S'", ["S"], 1, 0)

    return accepting_state in chart[n], chart


# Run parser
accepted, chart = earley_parser(sentence)

print("Sentence:")
print(" ".join(sentence))

print("\nEarley Parser Result:")

if accepted:
    print("Sentence accepted by the grammar.")
else:
    print("Sentence rejected by the grammar.")

print("\nChart States:")

for i, states in enumerate(chart):
    print("\nChart", i)

    for state in states:
        lhs, rhs, dot, origin = state

        before_dot = " ".join(rhs[:dot])
        after_dot = " ".join(rhs[dot:])

        print(
            f"{lhs} -> {before_dot} • {after_dot}, "
            f"origin={origin}"
        )