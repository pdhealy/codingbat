# # Version 1: My Attempt (working)
# def string_times(str, n):
#     if n >= 0:
#         return str * n

# Version 2:
def string_times(str, n):
    result = ""
    for i in range(n):
        result = result + str # Uses string concatenation to build the result. Creates a new string in memory each time.
    return result

if __name__ == "__main__":
    print(string_times('Hi', 2))  # Output: 'HiHi'
    print(string_times('Hi', 3))  # Output: 'HiHiHi'
    print(string_times('Hi', 1))  # Output: 'Hi'
    print(string_times('Hi', 0))  # Output: ''
    print(string_times('Hi', 5))  # Output: 'HiHiHiHiHi'
    print(string_times('Oh Boy!', 2))  # Output: 'Oh Boy!Oh Boy!'
    print(string_times('x', 4))  # Output: 'xxxx'
    print(string_times('', 4))  # Output: ''
    print(string_times('code', 2))  # Output: 'codecode'
    print(string_times('code', 3))  # Output: 'codecodecode'
