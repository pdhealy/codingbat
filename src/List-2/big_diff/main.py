# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.

# Version 1 (My Attempt)
def big_diff(nums):
  return max(nums) - min(nums)


# Version 2 (Optimized)
def big_diff(nums):
    smallest = nums[0]
    largest = nums[0]
    
    for n in nums:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    
    return largest - smallest


if __name__ == "__main__":
    # Example test cases
    print(big_diff([10, 3, 5, 6]))  # Output: 7
    print(big_diff([7, 2, 10, 9]))  # Output: 8
    print(big_diff([2, 10, 7, 2]))  # Output: 8
    print(big_diff([2, 10]))  # Output: 8
    print(big_diff([10, 2]))  # Output: 8
    print(big_diff([10, 0]))  # Output: 10
    print(big_diff([2, 3]))  # Output: 1
    print(big_diff([2, 2]))  # Output: 0
    print(big_diff([2]))  # Output: 0
    print(big_diff([5, 1, 6, 1, 9, 9]))  # Output: 8
    print(big_diff([7, 6, 8, 5]))  # Output: 3
    print(big_diff([7, 7, 6, 8, 5, 5, 6]))  # Output: 3
