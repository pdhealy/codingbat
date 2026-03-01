# Version 1 (Official):
def sleep_in(weekday: bool, vacation: bool) -> bool:
  if not weekday or vacation:
    return True
  else:
    return False
  # This can be shortened to: return(not weekday or vacation)

if __name__ == "__main__":
  # Example test cases
  print(sleep_in(False, False))  # → True
  print(sleep_in(True, False))   # → False
  print(sleep_in(False, True))   # → True
  print(sleep_in(True, True))    # → True