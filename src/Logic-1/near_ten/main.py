# Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

# Version 1 (My Attempt)
def near_ten(num):
  return num % 10 in (0, 1, 2, 8, 9)

# Version 2 (Optimized)
def near_ten(num):
  return num % 10 <= 2 or num % 10 >= 8

# Version 3 (Using Absolute Value)
def near_ten(num):
  return abs(num % 10) <= 2 or abs(num % 10) >= 8

# Version 4 (Using Modulo and Absolute Value) - Being within 2 of a multiple of 10 is equivalent to being within 2 of either 0 or 10. Handles the case when the multiple is below 10 as well.
def near_ten(num):
  return abs(num % 10) <= 2 or abs(num % 10 - 10) <= 2

if __name__ == "__main__":
    # Example test cases
    print(near_ten(12))  # Output: True
    print(near_ten(17))  # Output: False
    print(near_ten(19))  # Output: True
    print(near_ten(31))  # Output: True
    print(near_ten(6))  # Output: False
    print(near_ten(10))  # Output: True
    print(near_ten(11))  # Output: True
    print(near_ten(21))  # Output: True
    print(near_ten(22))  # Output: True
    print(near_ten(23))  # Output: False
    print(near_ten(54))  # Output: False
    print(near_ten(155))  # Output: False
    print(near_ten(158))  # Output: True
    print(near_ten(3))  # Output: False
    print(near_ten(1))  # Output: True
