from automathon import DFA
import string

def quote_special(char):
    if char.isalnum():
        return char
    return f'"{char}"'

def create_english_dfa():
    q = {'q0', 'q1', 'q_reject'}

    lowercase_letters = set(string.ascii_lowercase)
    uppercase_letters = set(string.ascii_uppercase)
    numbers = set(string.digits)
    special_chars_to_quote = {' ', '.', ',', '!', '?', '_', '-', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', '/', '~', '`'}

    special_chars = set(quote_special(c) for c in special_chars_to_quote)
    
    sigma = lowercase_letters | uppercase_letters | numbers | special_chars

    delta = {}

    #define transitions from all the states
    delta['q0'] = {}
    for char in lowercase_letters:
        delta['q0'][char] = 'q1'
    for char in uppercase_letters | numbers | special_chars:
        delta['q0'][char] = 'q_reject'

    delta['q1'] = {}
    for char in lowercase_letters:
        delta['q1'][char] = 'q1'
    for char in uppercase_letters | numbers | special_chars:
        delta['q1'][char] = 'q_reject'
    
    delta['q_reject'] = {}
    for char in sigma:
        delta['q_reject'][char] = 'q_reject'

    initial_state = 'q0'

    f = {'q1'}

    return DFA(q, sigma, delta, initial_state, f)

def test_input(automata, word):
    try:
        if automata.accept(word):
            return "Accepted"
        else:
            return "Not Accepted"
    except Exception:
        return "Not Accepted"
    
def main():
    automata = create_english_dfa()

    test_cases = [
        "cat",
        "dog", 
        "a",
        "zebra",
        "hello",
        "world",
        "programming",

        "dog1",        # contains digit
        "1dog",        # starts with digit
        "DogHouse",    # contains uppercase letters
        "Dog_house",   # contains underscore
        " cats",       # starts with space
        "Cat",         # starts with uppercase
        "hello world", # contains space
        "test@email",  # contains special character
        "",            # empty string
        "123",         # all digits
        "HELLO",       # all uppercase
        "hello!",
    ]

    for word in test_cases:
        result = test_input(automata, word)
        print(f"Input: {word}, Result: {result}")

    print("\nGenerating Visualization")
    automata.view("English_Word_DFA")

if __name__ == "__main__":
    main()

