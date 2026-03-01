# Version 1 (My Attempt): (working but incorrect)

def string_match(a, b):
    substr_set = set()
    count = 0

    for index in range(len(a) - 1):
        a_substr = a[index:index + 2]
        substr_set.add(a_substr)

    for index in range(len(b) - 1):
        b_substr = b[index:index + 2]
        if b_substr in substr_set:
            count += 1

    return count

# Version 2 (Official):
def string_match(a, b):
    shorter = min(len(a), len(b))
    count = 0

    for i in range(shorter - 1):
        a_sub = a[i:i + 2]
        b_sub = b[i:i + 2]
        if a_sub == b_sub:
            count += 1

    return count

if __name__ == "__main__":
    # Example test cases
    print(string_match('xxcaazz', 'xxbaaz'))  # Output: 3
    print(string_match('abc', 'abc'))  # Output: 2
    print(string_match('abc', 'axc'))  # Output: 0
    print(string_match('aabbccdd', 'abbbxxd')) # Output: 1
