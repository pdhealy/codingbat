# Version 1 (My attempt)
def first_half(str):
  if len(str) % 2 != 0:
    return "str contains an odd number of characters"

  str_mid = len(str) - (len(str) - (len(str) // 2))
  return str[:str_mid]

# Version 2 (Short)
def first_half(str):
  if len(str) % 2 != 0:
    return "str is not even length"

  return str[:(len(str) // 2)]

if __name__ == "__main__":
    # Example test case
    print(first_half('WooHoo'))  # Output: 'Woo'
    print(first_half('HelloThere'))  # Output: 'Hello'
    print(first_half('abcdef'))  # Output: 'abc'
    print(first_half('ab'))  # Output: 'a'
    print(first_half(''))  # Output: ''
    print(first_half('0123456789'))  # Output: '01234'
    print(first_half('kitten'))  # Output: 'kit'
