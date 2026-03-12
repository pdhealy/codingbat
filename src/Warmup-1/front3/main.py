# Version 1:
def front3(str):
    front_end = 3
    if len(str) < front_end:
        front_end = len(str)
    front = str[:front_end]
    return front + front + front

# # Version 2: My attempt (working)
# def front3(str):
#     if len(str) < 3:
#         return str[0:]*3  # Slice is silent for out-of-bound conditions
#     else:
#         return str[:3]*3

if __name__ == "__main__":
    print(front3('Java'))  # Output: #JavJavJav
    print(front3('Chocolate'))  # Output: 'ChoChoCho'
    print(front3('abc'))  # Output: 'abcabcabc'
    print(front3('abcXYZ'))  # Output: 'abcabcabc'
    print(front3('ab'))  # Output: 'ababab'
    print(front3('a'))  # Output: 'aaa'
    print(front3(''))  # Output: ''