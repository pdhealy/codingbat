# For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().

# Version 1 (My Attempt - working, but not accepted by CodingBat)
def round_sum(a, b, c):
  result = 0

  for num in (a, b, c):
    rounded_num = round10(num)
    result += rounded_num

  return result

def round10(num):
  num_str = str(num / 10)
  # Using string slicing to get the rightmost digit of the number after dividing by 10
  # CodingBat does not accept use of type conversion functions (I think), so not accepted by CodingBat
  num_right = int(num_str[-1])

  if num_right in range(5, 10):
    diff = 10 - num_right
    rounded_num = diff + num
  else:
    rounded_num = num - num_right

  return rounded_num

# Version 2 (Refactored - accepted by CodingBat)
def round_sum(a, b, c):
  result = 0

  for num in (a, b, c):
    rounded_num = round10(num)
    result += rounded_num

  return result

def round10(num):
  num_right = num % 10

  if num_right >= 5:
    diff = 10 - num_right
    rounded_num = diff + num
  else:
    rounded_num = num - num_right

  return rounded_num

if __name__ == "__main__":
    # Example test cases
    print(round_sum(16, 17, 18))  # Output: 60
    # round_sum(12, 13, 14) → 30	13	X
    print(round_sum(6, 4, 4))  # Output: 10
    # round_sum(4, 6, 5) → 20	5	X
    # round_sum(4, 4, 6) → 10	6	X
    # round_sum(9, 4, 4) → 10	4	X
    # round_sum(0, 0, 1) → 0	1	X
    # round_sum(0, 9, 0) → 10	0	X
    # round_sum(10, 10, 19) → 40	18	X
    # round_sum(20, 30, 40) → 90	36	X
    # round_sum(45, 21, 30) → 100	27	X
    # round_sum(23, 11, 26) → 60	24	X
    # round_sum(23, 24, 25) → 70	23	X
    # round_sum(25, 24, 25) → 80	23	X
    # round_sum(23, 24, 29) → 70	27	X
    # round_sum(11, 24, 36) → 70	33	X
    # round_sum(24, 36, 32) → 90	29	X
    # round_sum(14, 12, 26) → 50	24	X
    # round_sum(12, 10, 24) → 40	22	X
