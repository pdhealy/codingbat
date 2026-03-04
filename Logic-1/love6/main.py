# The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

# Version 1 (My Attempt)
def love6(a, b):
    sum = a + b
    diff = abs(a - b)

    if a == 6 or b == 6 or sum == 6 or diff == 6:
      return True
    else:
      return False

# Version 2 (Optimized)
def love6(a, b):
    return a == 6 or b == 6 or (a + b) == 6 or abs(a - b) == 6

if __name__ == "__main__":
    # Example test cases
    print(love6(6, 4))  # Output: True
    print(love6(4, 5))  # Output: False
    print(love6(1, 5))  # Output: True
    print(love6(1, 6))  # Output: True
    print(love6(1, 8))  # Output: False
    print(love6(1, 7))  # Output: True
    print(love6(7, 5))  # Output: False
    print(love6(8, 2))  # Output: True
    print(love6(6, 6))  # Output: True
    print(love6(-6, 2))  # Output: False
    print(love6(-4, -10))  # Output: True
    print(love6(-7, 1))  # Output: False
    print(love6(7, -1))  # Output: True
    print(love6(-6, 12))  # Output: True
    print(love6(-2, -4))  # Output: False
    print(love6(7, 1))  # Output: True
    print(love6(0, 9))  # Output: False
    print(love6(8, 3))  # Output: False
    print(love6(3, 3))  # Output: True
    print(love6(3, 4))  # Output: False
