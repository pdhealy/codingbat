# Version 1 (My Attempt:Working)
def make_abba(a, b):
    return a + b + b + a

# Version 2 (Using f-strings)
def make_abba(a, b):
    return f"{a}{b}{b}{a}"

if __name__ == "__main__":
    # Example test cases
    print(make_abba('Hi', 'Bye'))  # Output: 'HiByeByeHi'
    print(make_abba('Yo', 'Alice'))  # Output: 'YoAliceAliceYo'
    print(make_abba('What', 'Up'))  # Output: 'WhatUpUpWhat'
    print(make_abba('aaa', 'bbb'))  # Output: 'aaabbbbbbaaa'
    print(make_abba('x', 'y'))  # Output: 'xyyx'
    print(make_abba('x', ''))  # Output: 'xx'
    print(make_abba('', 'y'))  # Output: 'yy'
    print(make_abba('Bo', 'Ya'))  # Output: 'BoYaYaBo'
    print(make_abba('Ya', 'Ya'))  # Output: 'YaYaYaYa'
