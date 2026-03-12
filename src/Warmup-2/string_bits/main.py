# Version 1: My Attempt (working)
def string_bits(str):
    result = ""
    for index in range(0, len(str), 2):  # Uses step
        result = result + str[index]
    return result

# Version 2: My Attempt (working)
def string_bits(str):
    result = []
    for index in range(0, len(str), 2):
        result.append(str[index])
    return ''.join(result)

# Version 3:
def string_bits(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0: # Checks if the index is even
            result = result + str[i]
    return result

if __name__ == "__main__":
    print(string_bits('Hello'))  # Output: 'Hlo'
