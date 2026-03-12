# Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

# Version 1 (My Attempt)
def lone_sum(a, b, c):
  unique_nums = {}
  for num in (a, b, c):
    if num not in unique_nums:
      unique_nums[num] = 1
    else:
      unique_nums[num] += 1

  return sum(num for num, count in unique_nums.items() if count == 1)

# Version 2 (Solution)
def lone_sum(a, b, c):
  sum = 0
  if a != b and a != c:
    sum += a
  if b != a and b != c:
    sum += b
  if c != a and c != b:
    sum += c
  return sum

# Version 3 (Alternative Solution - similar to Version 1)
def lone_sum(a, b, c):
  unique_nums = {}
  sum = 0

  for num in (a, b, c):
    if num not in unique_nums:
      unique_nums[num] = 1
    else:
      unique_nums[num] += 1
  
  for num, count in unique_nums.items():
    if count == 1:
      sum += num

  return sum

if __name__ == "__main__":
    # Example test cases
    print(lone_sum(1, 2, 3))  # Output: 6
    print(lone_sum(3, 2, 3))  # Output: 2
    print(lone_sum(3, 3, 3))  # Output: 0
    print(lone_sum(9, 2, 2))  # Output: 9
    print(lone_sum(2, 2, 9))  # Output: 9
    print(lone_sum(2, 9, 2))  # Output: 9
    print(lone_sum(2, 9, 3))  # Output: 14
    print(lone_sum(4, 2, 3))  # Output: 9
    print(lone_sum(1, 3, 1))  # Output: 3
