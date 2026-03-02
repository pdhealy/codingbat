# When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

# Version 1 (My Attempt)
def cigar_party(cigars, is_weekend):
  if is_weekend and cigars >= 40:
    return True
  elif cigars >= 40 and cigars <=60:
    return True
  else:
    return False

# Version 2 (Optimized)
def cigar_party(cigars, is_weekend):
  if is_weekend:
    return cigars >= 40
  else:
    return 40 <= cigars <= 60

if __name__ == "__main__":
    # Example test cases
    print(cigar_party(30, False))  # Output: False
    print(cigar_party(50, False))  # Output: True
    print(cigar_party(70, True))  # Output: True
    print(cigar_party(30, True))  # Output: False
    print(cigar_party(50, True))  # Output: True
    print(cigar_party(60, False))  # Output: True
    print(cigar_party(61, False))  # Output: False
    print(cigar_party(40, False))  # Output: True
    print(cigar_party(39, False))  # Output: False
    print(cigar_party(40, True))  # Output: True
    print(cigar_party(39, True))  # Output: False
