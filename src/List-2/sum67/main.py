# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

# Version 1 (My Attempt - not working. See working version of for loop approach in Version 3 below)
def sum67(nums):
  total = 0

  found_6 = False
  found_7 = False

  for num in nums:
    if num == 6:
      found_6 = True
    elif num == 7:
      found_7 = True

    if found_6 and not found_7:
      continue
    else:
      total += num

  return total

# Version 2 (My 2nd Attempt, assisted by Codex)
def sum67(nums):
    total = 0
    i = 0

    while i < len(nums):
      if nums[i] == 6:
        while nums[i] != 7:
          i += 1
        i += 1
      else:
        total += nums[i]
        i += 1

    return total

# Version 3 (Codex)
def sum67(nums):
    total = 0
    ignore = False

    for num in nums:
      if num == 6:
        ignore = True
      elif num == 7 and ignore:
        ignore = False
      elif not ignore:
        total += num

    return total

if __name__ == "__main__":
    # Example test cases
    print(sum67([1, 2, 2]))  # Output: 5
    print(sum67([1, 2, 2, 6, 99, 99, 7])) # Output: 5
    print(sum67([1, 1, 6, 7, 2])) # Output: 4
    print(sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7])) # Output: 2
    print(sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7])) # Output: 2
    print(sum67([2, 7, 6, 2, 6, 7, 2, 7])) # Output: 18
    print(sum67([2, 7, 6, 2, 6, 2, 7])) # Output: 9
    print(sum67([1, 6, 7, 7])) # Output: 8
    print(sum67([6, 7, 1, 6, 7, 7])) # Output: 8
    print(sum67([6, 8, 1, 6, 7])) # Output: 0
    print(sum67([])) # Output: 0
    print(sum67([6, 7, 11])) # Output: 11
    print(sum67([11, 6, 7, 11])) # Output: 22
    print(sum67([2, 2, 6, 7, 7])) # Output: 11
