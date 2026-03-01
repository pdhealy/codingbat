# Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.

# Version 1 (My Attempt)
def same_first_last(nums):
    return len(nums) >= 1 and (nums[0] == nums[len(nums)-1])

# Version 2 (My Second Attempt)
def same_first_last(nums):
    if len(nums) >=1:
        if nums[0] == nums[len(nums)-1]:
            return True
    return False

# Version 3 (Optimized)
def same_first_last(nums):
    if not nums:
        return False

    return nums[0] == nums[-1]

if __name__ == "__main__":
    # Example test cases
    print(same_first_last([1, 2, 3]))  # Output: False
    print(same_first_last([1, 2, 3, 1]))  # Output: True
    print(same_first_last([1, 2, 1]))  # Output: True
    print(same_first_last([7]))  # Output: True
    print(same_first_last([]))  # Output: False
    print(same_first_last([1, 2, 3, 4, 5, 1]))  # Output: True
    print(same_first_last([1, 2, 3, 4, 5, 13]))  # Output: False
    print(same_first_last([13, 2, 3, 4, 5, 13]))  # Output: True
    print(same_first_last([7, 7]))  # Output: True
