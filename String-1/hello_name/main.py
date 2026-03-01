# Version 1 (My Attempt)
def hello_name(name):
    return "Hello " + name + '!'

# Version 2 (Using f-string)
def hello_name(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    # Example test cases:
    print(hello_name('Bob'))  # Output: 'Hello Bob!'
    print(hello_name('Alice'))  # Output: 'Hello Alice!'
    print(hello_name('X'))  # Output: 'Hello X!'