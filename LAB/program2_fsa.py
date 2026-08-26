def accepts_ending_with_ab(string):
    state = "q0"

    for ch in string:

        if state == "q0":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == "a":
                state = "q1"
            elif ch == "b":
                state = "q2"
            else:
                state = "q0"

        elif state == "q2":
            if ch == "a":
                state = "q1"
            else:
                state = "q0"

    return state == "q2"


strings = ["ab", "aab", "abab", "helloab", "abc", "abb"]

for string in strings:
    if accepts_ending_with_ab(string):
        print(string, "-> Accepted")
    else:
        print(string, "-> Rejected")