# Version 1: My Attempt (working)
def front_times(str, n):
    if n >= 0:
        if len(str) < 3:
            return str[0:] * n
        else:
            return str[:3] * n

# Version 2:
def front_times(str, n):
    front_len = 3
    if front_len > len(str):
        front_len = len(str)
    front = str[:front_len]

    result = ""
    for i in range(n):
        result = result + front
    return result

if __name__ == "__main__":
    print(front_times('Chocolate', 2))  # Output: 'ChoCho'
    print(front_times('Chocolate', 3))  # Output: 'ChoChoCho'
    print(front_times('Abc', 3))  # Output: 'AbcAbcAbc'
    print(front_times('Ab', 4))  # Output: 'AbAbAbAb'
    print(front_times('A', 4))  # Output: 'AAAA'
    print(front_times('', 4))  # Output: ''
    print(front_times('Abc', 0))  # Output: ''