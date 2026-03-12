# Version 1 (My Attempt)
def make_out_word(out, word):
    if len(out) % 2 != 0:
        return "Error: 'out' string must have an even length."
    out_mid = len(out) // 2
    # Remeber that string splicing is 0-based
    return out[:out_mid] + word + out[out_mid:]

if __name__ == "__main__":
    # Example test cases
    print(make_out_word('<<>>', 'Yay'))  # Output: '<<Yay>>'
    print(make_out_word('<<>>', 'WooHoo'))  # Output: '<<WooHoo>>'
    print(make_out_word('[[]]', 'word'))  # Output: '[[]word[]]'
    print(make_out_word('HHoo', 'Hello'))  # Output: 'HHHellooo'
    print(make_out_word('abyz', 'YAY'))  # Output: 'abYAYyz'
