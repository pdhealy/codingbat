# Given an int array length 2, return True if it contains a 2 or a 3.

# Version 1 (My Attempt)
def has23(nums):
    return (nums[0] == 2 or nums[0] == 3) or (nums[1] == 2 or nums[1] == 3)

# Version 2 (Optimized using 'in' keyword)
def has23(nums):
    return 2 in nums or 3 in nums

# Version 3
def has23(nums):
    for num in nums:
        if num == 2 or num == 3:
            return True
    return False

# Version 4 (Using set intersection)
def has23(nums):
    return bool(set(nums) & {2, 3})

# Version 5 (Using any() function)
def has23(nums):
    return any(num in (2, 3) for num in nums)

# Version 6 (Using list comprehension)
def has23(nums):
    return any([num for num in nums if num == 2 or num == 3])

if __name__ == "__main__":
    # Example test cases
    print(has23([2, 5]))  # Output: True
    print(has23([4, 3]))  # Output: True
    print(has23([4, 5]))  # Output: False
    print(has23([2, 2]))  # Output: True
    print(has23([3, 2]))  # Output: True
    print(has23([3, 3]))  # Output: True
    print(has23([7, 7]))  # Output: False
    print(has23([3, 9]))  # Output: True
    print(has23([9, 5]))  # Output: False
