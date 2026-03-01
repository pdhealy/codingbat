# Version 1 (My Attempt)
def extra_end(str):
  if len(str) < 2:
    return "Input str is too short"

  return str[-2:] * 3

if __name__ == "__main__":
    # Example test cases
    print(extra_end('Hello'))  # Output: 'lololo'
    print(extra_end('ab'))  # Output: 'ababab'
    print(extra_end('Hi'))  # Output: 'HiHiHi'
    print(extra_end('Candy'))  # Output: 'dydydy'
    print(extra_end('Code'))  # Output: 'dedede'
