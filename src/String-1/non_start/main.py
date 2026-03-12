# Version 1 (My Attempt)
def non_start(a, b):
  if len(a) < 1 or len(b) < 1:
    return "Input string with length 0 provided"
  
  return a[1:] + b[1:]

# Version 2 (Short)
def non_start(a, b):
  return a[1:] + b[1:]

if __name__ == "__main__":
    # Example test cases
    print(non_start('Hello', 'There'))  # Output: 'ellohere'
    print(non_start('java', 'code'))  # Output: 'avaode'
    print(non_start('shotl', 'java'))  # Output: 'hotlava'
    print(non_start('ab', 'xy'))  # Output: 'by'
    print(non_start('ab', 'x'))  # Output: 'b'
    print(non_start('x', 'ac'))  # Output: 'c'
    print(non_start('a', 'x'))  # Output: ''
    print(non_start('kit', 'kat'))  # Output: 'itat'
    print(non_start('mart', 'dart'))  # Output: 'artart'