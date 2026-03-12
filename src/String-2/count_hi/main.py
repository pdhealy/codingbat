# Return the number of times that the string "hi" appears anywhere in the given string.

# Version 1 (My Attempt)
def count_hi(str):
    count = 0

    for index in range(len(str) - 1):
        sub_str = str[index] + str[index + 1]

        if sub_str == "hi":
            count += 1

    return count

# Version 2 (Codex)
def count_hi(str):
    count = 0
    # Use range(len(s) - 1) so index + 1 is always safe
    for index in range(len(str) - 1):
        if str[index:index + 2] == "hi":
            count += 1
    return count

# Version 3 (Optimized)
def count_hi(str):
    count = 0
    index = 0

    while index < len(str) - 1:
        if str[index:index + 2] == "hi":
            count += 1
            index += 2  # Skip the next character since we found "hi"
        else:
            index += 1

    return count

if __name__ == "__main__":
    # Example test cases
    print(count_hi('abc hi ho'))  # Output: 1
    print(count_hi('ABChi hi'))  # Output: 2
    print(count_hi('hihi'))  # Output: 2
    print(count_hi('hiHIhi'))  # Output: 2
    print(count_hi(''))  # Output: 0
    print(count_hi('h'))  # Output: 0
    print(count_hi('hi'))  # Output: 1
    print(count_hi('Hi is no HI on ahI'))  # Output: 0
    print(count_hi('hiho not HOHIhi'))  # Output: 2
