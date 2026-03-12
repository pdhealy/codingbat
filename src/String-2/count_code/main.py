# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# Version 1 (My Attempt)
def count_code(str):
    count = 0

    for index in range(len(str) - 3):
        if str[index : index + 2] == "co":
            if str[index + 3] == "e":
                count += 1

    return count


# Version 2 (Optimized)
def count_code(str):
    count = 0

    for index in range(len(str) - 3):
        if str[index : index + 2] == "co" and str[index + 3] == "e":
            count += 1

    return count


# Version 3 (Using a `while` loop)
def count_code(str):
    count = 0
    index = 0

    while index < len(str) - 3:
        if str[index : index + 2] == "co":
            if str[index + 3] == "e":
                count += 1

        index += 1

    return count


if __name__ == "__main__":
    # Example test cases
    print(count_code("aaacodebbb"))  # Output: 1
    print(count_code("codexxcode"))  # Output: 2
    print(count_code("cozexxcope"))  # Output: 2
    print(count_code("cozfxxcope"))  # Output: 1
    print(count_code("xxcozeyycop"))  # Output: 1
    print(count_code("cozcop"))  # Output: 0
    print(count_code("abcxyz"))  # Output: 0
    print(count_code("code"))  # Output: 1
    print(count_code("ode"))  # Output: 0
    print(count_code("c"))  # Output: 0
    print(count_code(""))  # Output: 0
    print(count_code("AAcodeBBcoleCCccoreDD"))  # Output: 3
    print(count_code("AAcodeBBcoleCCccorfDD"))  # Output: 2
    print(count_code("coAcodeBcoleccoreDD"))  # Output: 3
