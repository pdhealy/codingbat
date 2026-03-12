# Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

# Version 1 (My Attempt)
def in1to10(n, outside_mode):
  if outside_mode:
    if n not in range(2, 10):
      return True
    else:
      return False
  elif not outside_mode:
    if n in range(1, 10+1):
      return True
    else:
      return False
  else:
    return False

# Version 2 (Optimized)
def in1to10(n, outside_mode):
  if outside_mode:
    return n <= 1 or n >= 10
  else:
    return 1 <= n <= 10

if __name__ == "__main__":
    # Example test cases
    print(in1to10(5, False))  # Output: True
    print(in1to10(11, False))  # Output: False
    print(in1to10(11, True))  # Output: True
    print(in1to10(10, False))  # Output: True
    print(in1to10(10, True))  # Output: True
    print(in1to10(9, False))  # Output: True
    print(in1to10(9, True))  # Output: False
    print(in1to10(1, False))  # Output: True
    print(in1to10(1, True))  # Output: True
    print(in1to10(0, False))  # Output: False
    print(in1to10(0, True))  # Output: True
    print(in1to10(-1, False))  # Output: False
    print(in1to10(-1, True))  # Output: True
    print(in1to10(99, False))  # Output: False
    print(in1to10(-99, True))  # Output: True
