# We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be done.

# Version 1 (My Attempt - not working)
def make_chocolate(small, big, goal):
  # If all small and big bars combined is less than goal then return -1
  if (small + (big * 5)) < goal:
    return -1
  elif goal % 5 == 0:
    return 0
  elif goal < (big * 5) and big > 0:
    diff = goal - 5
    if small >= diff:
      return diff
  elif goal > (big * 5):
    diff = goal - (big * 5)
    if small >= diff:
      return diff
  else:
    return 0

# Version 2 (Solution from CodingBat)
def make_chocolate(small, big, goal):
  # Calculalte the maximum number of big bars we can use without exceeding the goal
  max_big = goal // 5
  # If the number of big bars we have is less than the maximum we can use, then use all the big bars we have
  if max_big > big:
    max_big = big
  rem = goal - max_big * 5
  # If the remainder required is more than the small bars we have, then return -1
  if rem > small:
    return -1
  else:
    return rem

if __name__ == "__main__":
    # Example test cases
    print(make_chocolate(4, 1, 9))  # Output: 4
    print(make_chocolate(4, 1, 10))  # Output: -1
    print(make_chocolate(4, 1, 7))  # Output: 2
    print(make_chocolate(6, 2, 7))  # Output: 2
    print(make_chocolate(4, 1, 5))  # Output: 0
    print(make_chocolate(4, 1, 4))  # Output: 4
    print(make_chocolate(5, 4, 9))  # Output: 4
    print(make_chocolate(9, 3, 18))  # Output: 3
    print(make_chocolate(3, 1, 9))  # Output: -1
    print(make_chocolate(1, 2, 7))  # Output: -1
    print(make_chocolate(1, 2, 6))  # Output: 1
    print(make_chocolate(1, 2, 5))  # Output: 0
    print(make_chocolate(6, 1, 10))  # Output: 5
    print(make_chocolate(6, 1, 11))  # Output: 6
    print(make_chocolate(6, 1, 12))  # Output: -1
    print(make_chocolate(6, 1, 13))  # Output: -1
    print(make_chocolate(6, 2, 10))  # Output: 0
    print(make_chocolate(6, 2, 11))  # Output: 1
    print(make_chocolate(6, 2, 12))  # Output: 2
    print(make_chocolate(60, 100, 550))  # Output: 50
    print(make_chocolate(1000, 1000000, 5000006))  # Output: 6
    print(make_chocolate(7, 1, 12))  # Output: 7
    print(make_chocolate(7, 1, 13))  # Output: -1
    print(make_chocolate(7, 2, 13))  # Output: 3
