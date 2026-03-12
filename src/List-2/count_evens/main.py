# Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.

# Version 1 (My Attempt)
def count_evens(nums):
  count = 0

  for num in nums:
    if num % 2 == 0:
      count += 1

  return count

# Version 2 (Using generator expression and sum())
def count_evens(nums):
  return sum(1 for num in nums if num % 2 == 0)

if __name__ == "__main__":
    # Example test cases
    print(count_evens([2, 1, 2, 3, 4]))  # Output: 3
    print(count_evens([2, 2, 0]))  # Output: 3
    print(count_evens([1, 3, 5]))  # Output: 0
    print(count_evens([]))  # Output: 0
    print(count_evens([11, 9, 0, 1]))  # Output: 1
    print(count_evens([2, 11, 9, 0]))  # Output: 2
    print(count_evens([2]))
    print(count_evens([2, 5, 12]))  # Output: 2