# Version 1 (Official):
def last2(str):
    # If length of string is less than 2 then exit
    if len(str) < 2:
        return 0

    count = 0
    last2 = str[-2:]  # can also be written as `str[len(str)-2:]`
    for i in range(len(str) - 2):
        sub_str = str[i:i+2]  # Gets all substrings of lenght 2
        if sub_str == last2:
            count += 1
    return count

if __name__ == "__main__":
    print(last2('hixxhi'))  # Output: 1
    print(last2('xaxxaxaxx'))  # Output: 1
    print(last2('axxxaaxx'))  # Output: 2
    print(last2('xxaxxaxxaxx'))  # Output: 3
    print(last2('xaxaxaxx'))  # Output: 0
    print(last2('xxxx'))  # Output: 2
    print(last2('13121312'))  # Output: 1
    print(last2('11212'))  # Output: 1
    print(last2('13121311'))  # Output: 0
    print(last2('1717171'))  # Output: 2
    print(last2('hi'))  # Output: 0
    print(last2('h'))  # Output: 0
    print(last2(''))  # Output: 0
