# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

# Version 1 (My Attempt): (working)
"""
def array123(nums):
    curr_num = 0

    for num in nums:
        if num == curr_num + 1:
            curr_num += 1
        else:
            curr_num = 0
            if num == 1:  # Reset and check if current num starts a new sequence
                curr_num = 1
        if curr_num == 3:
            return True
    return False
"""

# Version 1 (Copilot):
# Using a `while` loop
def array123(nums):
    curr_num = 0
    i = 0

    while i < len(nums) and curr_num != 3:
        if nums[i] == curr_num + 1:
            curr_num += 1
        else:
            curr_num = 0
            if nums[i] == 1:
                curr_num = 1
        i += 1

    return curr_num == 3

# Run this code block only if this file is the main program being executed, not when imported as a module
if __name__ == "__main__":
    # Example test cases
    print(array123([1, 1, 2, 3, 1]))  # Output: True
    print(array123([1, 1, 2, 4, 1]))  # Output: False
    print(array123([1, 1, 2, 1, 2, 3]))  # Output: True
    print(array123([1, 1, 2, 1, 2, 1]))  # Output: False
    print(array123([1, 2, 3, 1, 2, 3]))  # Output: True
    print(array123([1, 2, 3]))  # Output: True
    print(array123([1, 1, 1]))  # Output: False
    print(array123([1, 2]))  # Output: False
    print(array123([1]))  # Output: False
    print(array123([]))  # Output: False