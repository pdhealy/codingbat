# Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.

# Version 1 (My Attempt)
def close_far(a, b, c):
  if abs(a - b) <= 1:
    if abs(c - b) >= 2 and abs(c - a) >= 2:
      return True
    else:
      return False
  elif abs(a - c) <= 1:
    if abs(b - c) >= 2 and abs(b - a) >= 2:
      return True
    else:
      return False
  else:
    return False

# Version 2 (Optimized)
def close_far(a, b, c):
    close_b = abs(a - b) <= 1
    close_c = abs(a - c) <= 1
    far_b = abs(b - c) >= 2 and abs(b - a) >= 2
    far_c = abs(c - b) >= 2 and abs(c - a) >= 2
    
    return (close_b and far_c) or (close_c and far_b)

if __name__ == "__main__":
    # Example test cases
    print(close_far(1, 2, 10))  # Output: True
    print(close_far(1, 2, 3))  # Output: False
    print(close_far(4, 1, 3))  # Output: True
    print(close_far(4, 5, 3))  # Output: False
    print(close_far(4, 3, 5))  # Output: False
    print(close_far(-1, 10, 0))  # Output: True
    print(close_far(0, -1, 10))  # Output: True
    print(close_far(10, 10, 8))  # Output: True
    print(close_far(10, 8, 9))  # Output: False
    print(close_far(8, 9, 10))  # Output: False
    print(close_far(8, 9, 7))  # Output: False
    print(close_far(8, 6, 9))  # Output: True
