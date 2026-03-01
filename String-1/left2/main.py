# Version 1 (My Attempt)
def left2(str):
    return str[2:] + str[:2]

# Version 2 (Longer)
def left2(str):
    first_2 = len(str) - (len(str) - 2)
    return str[2:] + str[:first_2]

if __name__ == "__main__":
    # Example test cases
    print(left2('Hello'))  # Output: 'lloHe'
    print(left2('java'))  # Output: 'vaja'
    print(left2('Hi'))  # Output: 'Hi'
    print(left2('code'))  # Output: 'deco'
    print(left2('cat'))  # Output: 'tca'
    print(left2('12345'))  # Output: '34512'
    print(left2('Chocolate'))  # Output: 'ocolateCh'
    print(left2('bricks'))  # Output: 'icksbr'
