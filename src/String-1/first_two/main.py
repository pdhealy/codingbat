# Version 1 (My Attempt): Using a `while` loop
def first_two(str):
  new_str = ""
  i = 0

  while i < len(str) and i < 2:
    for f in range(i, i + 1):
      new_str = new_str + str[f]
      i += 1
  return new_str

# Version 2 (Solution): Using string slicing
def first_two(str):
  if len(str) < 2:
    return str
  else:
    # This is the same as str[:2] but is more complex to understand. 
    # We're first subtracting the length of the string from 2 to get the number of characters we want to keep, then we subtract that from the total length of the string to get the index of the last character we want to keep.
    return str[:len(str) - (len(str) - 2)]

if __name__ == "__main__":
    # Example test cases
    print(first_two('Hello'))  # Output: 'He'
    print(first_two('abcdefg'))  # Output: 'ab'
    print(first_two('ab'))  # Output: 'ab'
