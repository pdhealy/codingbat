# The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.

# Version 1 (My Attempt)
def squirrel_play(temp, is_summer):
  if is_summer:
    return 60 <= temp <= 100
  else:
    return 60 <= temp <= 90
  
# Version 2 (Optimized)
def squirrel_play(temp, is_summer):
  upper_limit = 100 if is_summer else 90
  return 60 <= temp <= upper_limit

if __name__ == "__main__":
    # Example test cases
    print(squirrel_play(70, False))  # Output: True
    print(squirrel_play(95, False))  # Output: False
    print(squirrel_play(95, True))  # Output: True
    print(squirrel_play(90, False))  # Output: True
    print(squirrel_play(90, True))  # Output: True
    print(squirrel_play(50, False))  # Output: False
    print(squirrel_play(50, True))  # Output: False
    print(squirrel_play(100, False))  # Output: False
    print(squirrel_play(100, True))  # Output: True
    print(squirrel_play(105, True))  # Output: False
    print(squirrel_play(59, False))  # Output: False
    print(squirrel_play(59, True))  # Output: False
    print(squirrel_play(60, False))  # Output: True
