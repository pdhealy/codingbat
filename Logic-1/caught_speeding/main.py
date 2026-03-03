# You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

# Version 1 (My Attempt)
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed = speed - 5

  if 61 <= speed <= 81:
    return 1
  elif speed > 81:
    return 2
  else:
    return 0

# Version 2 (Optimized)
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5

  if speed <= 60:
    return 0
  elif speed <= 80:
    return 1
  else:
    return 2

# Version 3 (Ternary Operator)
def caught_speeding(speed, is_birthday):
  if is_birthday:
    speed -= 5

  return 0 if speed <= 60 else 1 if speed <= 80 else 2

if __name__ == "__main__":
    # Example test cases
    print(caught_speeding(60, False))  # Output: 0
    print(caught_speeding(65, False))  # Output: 1
    print(caught_speeding(65, True))   # Output: 0
    print(caught_speeding(80, False))  # Output: 1
    print(caught_speeding(85, False))  # Output: 2
    print(caught_speeding(85, True))   # Output: 1
    print(caught_speeding(70, False))  # Output: 1
    print(caught_speeding(75, False))  # Output: 1
    print(caught_speeding(75, True))   # Output: 1
    print(caught_speeding(40, False))  # Output: 0
    print(caught_speeding(40, True))   # Output: 0
    print(caught_speeding(90, False))  # Output: 2
