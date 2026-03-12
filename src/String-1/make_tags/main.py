# Version 1 (My Attempt)
def make_tags(tag, word):
    opening = "<" + tag + ">"
    closing = "</" + tag + ">"
    return opening + word + closing

if __name__ == "__main__":
    # Example test cases
    print(make_tags('i', 'Yay'))  # Output '<i>Yay</i>'
    print(make_tags('i', 'Hello'))  # Output '<i>Hello</i>'
    print(make_tags('cite', 'Yay'))  # Output '<cite>Yay</cite>'
    print(make_tags('address', 'here'))  # Output '<address>here</address>'
    print(make_tags('body', 'Heart'))  # Output '<body>Heart</body>'
    print(make_tags('i', 'i'))  # Output '<i>i</i>'
    print(make_tags('i', ''))  # Output '<i></i>'
