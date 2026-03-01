# Version 1 (My Attempt):
def without_end(str):
    if len(str) < 2:
        return "str is too small"

    return str[1 : -1]

# Version 2 (Longer):
def without_end(str):
    if len(str) < 2:
        return "str is too small"

    # Calculate the starting and ending indices for slicing
    start = len(str) - (len(str) - 1)
    end = len(str) - 1
    return str[start : end]

if __name__ == "__main__":
    # Example test cases
    print(without_end('Hello'))  # Output: 'ell'
    print(without_end('java'))  # Output: 'av'
    print(without_end('coding'))  # Output: 'odin'
