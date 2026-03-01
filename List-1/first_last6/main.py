# Version 1 (My Attempt)
def first_last6(nums):
    if len(nums) < 1:
        return False

    return (nums[0] == 6) or (nums[len(nums)-1] == 6)

# Version 2 (Optimized)
def first_last6(nums):
    if not nums:
        return False

    return nums[0] == 6 or nums[-1] == 6

# Version 3 (Using any() function)
def first_last6(nums):
    if not nums:
        return False

    return any(x == 6 for x in (nums[0], nums[-1]))

# Version 4 (Using set for O(1) lookup)
def first_last6(nums):
    if not nums:
        return False

    return 6 in {nums[0], nums[-1]}

if __name__ == "__main__":
    # Example test cases
    print(first_last6([1,2,6]))  # Output: True
    print(first_last6([6, 1, 2, 3]))  # Output: True
    print(first_last6([13, 6, 1, 2, 3]))  # Output: False
    print(first_last6([13, 6, 1, 2, 6]))  # Output: True
    print(first_last6([3, 2, 1]))  # Output: False
    print(first_last6([3, 6, 1]))  # Output: False
    print(first_last6([3, 6]))  # Output: True
    print(first_last6([6]))  # Output: True
    print(first_last6([3]))  # Output: False
    print(first_last6([3]))  # Output: False
    print(first_last6([5, 6]))  # Output: True
    print(first_last6([5, 5]))  # Output: False
    print(first_last6([1, 2, 3, 4, 6]))  # Output: True
    print(first_last6([1, 2, 3, 4]))  # Output: False