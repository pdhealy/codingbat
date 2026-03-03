# Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

# Version 1 (My Attempt)
def sorta_sum(a, b):
  sum = a + b

  if sum in range(10, 20):
    return 20
  else:
    return sum
  
  # Version 2 (Optimized)
def sorta_sum(a, b):
  sum = a + b

  return 20 if sum in range(10, 20) else sum

# Version 3 (Ternary Operator)
def sorta_sum(a, b):
  sum = a + b

  return 20 if 10 <= sum <= 19 else sum

if __name__ == "__main__":
    # Example test cases
    print(sorta_sum(3, 4))  # Output: 7
    print(sorta_sum(9, 4))  # Output: 20
    print(sorta_sum(10, 11))  # Output: 21
    print(sorta_sum(12, -3))  # Output: 9
    print(sorta_sum(-3, 12))  # Output: 9
    print(sorta_sum(4, 5))  # Output: 9
    print(sorta_sum(4, 6))  # Output: 20
    print(sorta_sum(14, 7))  # Output: 21
    print(sorta_sum(14, 6))  # Output: 20
