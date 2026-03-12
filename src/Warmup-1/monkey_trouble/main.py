# Example 1:
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  elif not a_smile and not b_smile: # Another way to view `not True` and `not True` is:- if `False` and `False`
    return True
  return False

# # Example 2:
# def monkey_trouble(a_smile, b_smile):
#    return ((a_smile and b_smile) or (not a_smile and not b_smile))

# # Example 3:
# def monkey_trouble(a_smile, b_smile):
#    return (a_smile == b_smile)
#   ## Or this very short version (think about how this is the same as the above)

if __name__ == "__main__":
    print(monkey_trouble(True, True))  #True
    print(monkey_trouble(False, False))  #True
    print(monkey_trouble(True, False))  #False
    print(monkey_trouble(False, True))  #False