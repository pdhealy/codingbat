# Given a string, return a string where for every char in the original, there are two chars.

# Version 1 (My Attempt)
# For large inputs, the list approach (Version 1 and 2) is both faster and uses less memory.
def double_char(str):
  new_str = []

  for char in str:
    new_str.append(char * 2)

  return ''.join(new_str)

# Version 2 (Using List Comprehension)
def double_char(str):
  return ''.join([char * 2 for char in str])

# Version 3 (Optimized Version)
# Using string concatenation in a loop generally uses more memory and is less efficient than building a list and joining at the end
def double_char(str):
  result = ""
  for char in str:
    result += char * 2
  return result

if __name__ == "__main__":
    # Example test cases
    print(double_char('The'))  # Output: 'TThhee'
    print(double_char('AAbb'))  # Output: 'AAAAbbbb'
    print(double_char('Hi-There'))  # Output: 'HHii--TThheerree'
    print(double_char('Word!'))  # Output: 'WWoorrdd!!'
    print(double_char('!!'))  # Output: '!!!!'
    print(double_char(''))  # Output: ''
    print(double_char('a'))  # Output: 'aa'
    print(double_char('.'))  # Output: '..'
    print(double_char('aa'))  # Output: 'aaaa'
