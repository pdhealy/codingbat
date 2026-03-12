# Version 1 (My Attempt)
def combo_string(a, b):
  if len(a) == len(b):
    return "Strings a and b are same length"

  if len(a) < len(b):
    short, long = a, b
  else:
    short, long = b, a

  return short + long + short

# Version 2 (Solution)
def combo_string(a, b):
  if len(a) < len(b):
    return a + b + a
  else:
    return b + a + b

if __name__ == "__main__":
    # Example test cases
    print(combo_string('Hello', 'hi'))  # Output: 'hiHellohi'
    print(combo_string('hi', 'Hello'))  # Output: 'hiHellohi'
    print(combo_string('aaa', 'b'))  # Output: 'baaab'
    print(combo_string('b', 'aaa'))  # Output: 'baaab'
    print(combo_string('aaa', ''))  # Output: 'aaa'
    print(combo_string('', 'bb'))  # Output: 'bb'
    print(combo_string('aaa', '1234'))  # Output: 'aaa1234aaa'
    print(combo_string('aaa', 'bb'))  # Output: 'bbaaabb'
    print(combo_string('a', 'bb'))  # Output: 'abba'
    print(combo_string('bb', 'a'))  # Output: 'abba'
    print(combo_string('xyz', 'ab'))  # Output: 'abxyzab'
