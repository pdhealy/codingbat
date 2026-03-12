# Given an array of ints length 3, return the sum of all the elements.

# Version 1 (My Attempt)
def sum3(nums):
  sum = 0
  for num in nums:
    sum += num
  return sum

# Version 2 (Optimized)
def sum3(nums):
  return sum(nums)

if __name__ == "__main__":
    # Example test cases
    print(sum3([1, 2, 3]) == 6)
    print(sum3([5, 11, 2]) == 18)
    print(sum3([7, 0, 0]) == 7)
    print(sum3([1, 2, 1]) == 4)
    print(sum3([1, 1, 1]) == 3)
    print(sum3([2, 7, 2]) == 11)
