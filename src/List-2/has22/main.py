# Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.

# Version 1 (My Attempt)

def has22(nums):
    # Be careful with off-by-one loop boundaries (i.e., len(nums)+1))
    for index in range(len(nums) - 1):
        if nums[index] == 2:
            if nums[index + 1] == nums[index]:
                return True
        continue
    return False

# Version 2 (Optimized)

def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False

# Version 3 (Concise)
# Uses the zip function to pair each element with the next one and checks for the condition in a single line.
def has22(nums):
    return any(a == 2 and b == 2 for a, b in zip(nums, nums[1:]))


if __name__ == "__main__":
    # Example test cases
    print(has22([1, 2, 2]))  # Output: True
    print(has22([1, 2, 1, 2]))  # Output: False
    print(has22([2, 1, 2]))  # Output: False
    print(has22([2, 2, 1, 2]))  # Output: True
    print(has22([1, 3, 2]))  # Output: False
    print(has22([1, 3, 2, 2]))  # Output: True
    print(has22([2, 3, 2, 2]))  # Output: True
    print(has22([4, 2, 4, 2, 2, 5]))  # Output: True
    print(has22([1, 2]))  # Output: False
    print(has22([2, 2]))  # Output: True
    print(has22([2]))  # Output: False
    print(has22([]))  # Output: False
    print(has22([3, 3, 2, 2]))  # Output: True
    print(has22([5, 2, 5, 2]))  # Output: False
