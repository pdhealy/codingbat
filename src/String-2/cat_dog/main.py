# Return True if the string "cat" and "dog" appear the same number of times in the given string.

# Version 1 (My Attempt)
def cat_dog(str):
  count_cat = 0
  count_dog = 0

  for index in range(len(str) - 1):

    if str[index] == 'c':
      if str[index:index + 3] == 'cat':
        count_cat += 1
    elif str[index] == 'd':
      if str[index:index + 3] == 'dog':
        count_dog += 1

  return count_cat == count_dog

# Version 2 (Optimized)
def cat_dog(str):
  count_cat = str.count('cat')
  count_dog = str.count('dog')
  return count_cat == count_dog

# Version 3 (One-liner)
def cat_dog(str):
    return str.count('cat') == str.count('dog')

if __name__ == "__main__":
    # Example test cases
    print(cat_dog('catdog'))  # Output: True
    print(cat_dog('catcat'))  # Output: False
    print(cat_dog('1cat1cadodog'))  # Output: True
    print(cat_dog('catxxdogxxxdog'))  # Output: False
    print(cat_dog('catxdogxdogxcat'))  # Output: True
    print(cat_dog('catxdogxdogxca'))  # Output: False
    print(cat_dog('dogdogcat'))  # Output: False
    print(cat_dog('dogogcat'))  # Output: True
    print(cat_dog('dog'))  # Output: False
    print(cat_dog('cat'))  # Output: False
    print(cat_dog('ca'))  # Output: True
    print(cat_dog('c'))  # Output: True
    print(cat_dog(''))  # Output: True
