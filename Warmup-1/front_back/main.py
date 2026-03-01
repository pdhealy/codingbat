# Version 1:
def front_back(str):
    if len(str) <= 1:
        return str

    mid = str[1:-1] # can be written as str[1:len(str)-1]

    return str[len(str)-1] + mid + str[0]

# # Version 2: My attempt (not correct)
# def front_back(str):
#     front = str[:1]
#     back = str[-1:]
#     middle = str[1:-1]
#     return back + middle + front

if __name__ == "__main__":
    print(front_back('code'))  # Output: 'eodc'
    print(front_back('a'))     # Output: 'a'
    print(front_back('ab'))    # Output: 'ba'
    print(front_back('abc'))   # Output: 'cba'
    print(front_back(''))      # Output: ''
    print(front_back('Chocolate'))  # Output: 'ehocolatC'
    print(front_back('aavJ'))  # Output: 'Java'
    print(front_back('hello'))  # Output: 'oellh'
