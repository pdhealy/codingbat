# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

# Version 1 (My Attempt - not working)
def make_bricks(small, big, goal):
  remainder = goal - small
  if remainder == 0 or (goal % (big * 5)) == 0:
    return True
  elif big > 0 and remainder >= 0:
    if remainder % 5 == 0 and (remainder / 5) <= big:
      return True
  else:
    return False

# Version 2 (Solution)
def make_bricks(small, big, goal):
  # Return False if the total length of all bricks is less than the goal
  if small + big * 5 < goal:
    return False
  elif small >= goal % 5:
    return True
  else:
    return False

# Version 3 (More concise)
def make_bricks(small, big, goal):
  return small + big * 5 >= goal and small >= goal % 5

if __name__ == "__main__":
    # Example test cases
    print(make_bricks(3, 1, 8))  # Output: True
    print(make_bricks(3, 1, 9))  # Output: False
    print(make_bricks(3, 2, 10))  # Output: True
    print(make_bricks(3, 2, 8))  # Output: True
    print(make_bricks(3, 2, 9))  # Output: False
    print(make_bricks(6, 1, 11))  # Output: True
    print(make_bricks(6, 0, 11))  # Output: False
    print(make_bricks(1, 4, 11))  # Output: True
    print(make_bricks(0, 3, 10))  # Output: True
    print(make_bricks(1, 4, 12))  # Output: False
    print(make_bricks(3, 1, 7))  # Output: True
    print(make_bricks(1, 1, 7))  # Output: False
    print(make_bricks(2, 1, 7))  # Output: True
    print(make_bricks(7, 1, 11))  # Output: True
    print(make_bricks(7, 1, 8))  # Output: True
    print(make_bricks(7, 1, 13))  # Output: False
    print(make_bricks(43, 1, 46))  # Output: True
    print(make_bricks(40, 1, 46))  # Output: False
    print(make_bricks(40, 2, 47))  # Output: True
    print(make_bricks(40, 2, 50))  # Output: True
    print(make_bricks(40, 2, 52))  # Output: False
    print(make_bricks(22, 2, 33))  # Output: False
    print(make_bricks(0, 2, 10))  # Output: True
    print(make_bricks(1000000, 1000, 1000100))  # Output: True
    print(make_bricks(2, 1000000, 100003))  # Output: False
    print(make_bricks(20, 0, 19))  # Output: True
    print(make_bricks(20, 0, 21))  # Output: False
    print(make_bricks(20, 4, 51))  # Output: False
    print(make_bricks(20, 4, 39))  # Output: True
