# Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

# Version 1 (My Attempt)
def lucky_sum(a, b, c):
  sum = 0

  for num in (a, b, c):
    if num != 13:
      sum += num
    else:
      return sum

  return sum

# Version 2 (Optimized)
def lucky_sum(a, b, c):
  sum = 0

  for num in (a, b, c):
    if num == 13:
      break
    sum += num

  return sum

if __name__ == "__main__":
    # Example test cases
    print(lucky_sum(1, 2, 3))  # Output: 6
    print(lucky_sum(1, 2, 13))  # Output: 3
    print(lucky_sum(1, 13, 3))  # Output: 1
    print(lucky_sum(1, 13, 13))  # Output: 1
    print(lucky_sum(6, 5, 2))  # Output: 13
    print(lucky_sum(13, 2, 3))  # Output: 0
    print(lucky_sum(13, 2, 13))  # Output: 0
    print(lucky_sum(13, 13, 2))  # Output: 0
    print(lucky_sum(9, 4, 13))  # Output: 13
    print(lucky_sum(8, 13, 2))  # Output: 8
    print(lucky_sum(7, 2, 1))  # Output: 10
    print(lucky_sum(3, 3, 13))  # Output: 6
