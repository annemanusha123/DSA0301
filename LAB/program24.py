# Simple Dialog Act Recognition

def recognize_dialog_act(sentence):

    text = sentence.lower().strip()

    # Greeting
    if any(word in text for word in ["hello", "hi", "hey", "good morning"]):
        return "GREETING"

    # Goodbye
    elif any(word in text for word in ["bye", "goodbye", "see you"]):
        return "GOODBYE"

    # Question
    elif text.endswith("?") or text.startswith(
        ("what", "why", "when", "where", "who", "how", "is", "are", "do", "does")
    ):
        return "QUESTION"

    # Request
    elif any(word in text for word in ["please", "could you", "can you"]):
        return "REQUEST"

    # Answer / Information
    elif any(word in text for word in ["yes", "no", "because", "the answer"]):
        return "ANSWER"

    # Default
    else:
        return "STATEMENT"


# Sample conversation
dialogue = [
    "Hello!",
    "How are you?",
    "Can you help me with my NLP assignment?",
    "Yes, I can help you.",
    "Thank you.",
    "Goodbye!"
]

print("Dialog Act Recognition")
print("----------------------")

for sentence in dialogue:
    act = recognize_dialog_act(sentence)

    print("\nSentence:", sentence)
    print("Dialog Act:", act)