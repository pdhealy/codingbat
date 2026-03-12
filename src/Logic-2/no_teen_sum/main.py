# Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

# Version 1 (My Attempt)
def no_teen_sum(a, b, c):
  sum = 0

  for num in (a, b, c):
    value = fix_teen(num)
    sum += value

  return sum

def fix_teen(num):
  if num in range(13, 20) and num not in range(15, 17):
    return 0
  else:
    return num

# Version 2 (Optimized)
def no_teen_sum(a, b, c):
  sum = 0

  for num in (a, b, c):
    if num in range(13, 20) and num not in range(15, 17):
      # If the number is a teen (13..19) but not 15 or 16, skip it because it counts as 0
      continue
    sum += num

  return sum

if __name__ == "__main__":
    # Example test cases
    print(no_teen_sum(1, 2, 3))  # Output: 6
    print(no_teen_sum(2, 13, 1))  # Output: 3
    print(no_teen_sum(2, 1, 14))  # Output: 3
    print(no_teen_sum(2, 1, 15))  # Output: 18
    print(no_teen_sum(2, 1, 16))  # Output: 19
    print(no_teen_sum(2, 1, 17))  # Output: 3
    print(no_teen_sum(17, 1, 2))  # Output: 3
    print(no_teen_sum(2, 15, 2))  # Output: 19
    print(no_teen_sum(16, 17, 18))  # Output: 16
    print(no_teen_sum(17, 18, 19))  # Output: 0
    print(no_teen_sum(15, 16, 1))  # Output: 32
    print(no_teen_sum(15, 15, 19))  # Output: 30
    print(no_teen_sum(15, 19, 16))  # Output: 31
    print(no_teen_sum(5, 17, 18))  # Output: 5
    print(no_teen_sum(17, 18, 16))  # Output: 16
    print(no_teen_sum(17, 19, 18))  # Output: 0