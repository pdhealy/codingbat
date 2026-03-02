# Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.

# Version 1 (My Attempt)
def make_ends(nums):
    return [nums[0], nums[-1]]

# Version 2 (Using a `for` loop)
def make_ends(nums):
    if len(nums) == 1:
        return [nums[0], nums[0]]

    output = []
    for i in range(len(nums)):
        if i == 0 or i == (len(nums) - 1):
            output.append(nums[i])
    return output

# Version 3 (Optimized - Similar to Version 1)
def make_ends(nums):
    return [nums[0], nums[len(nums) - 1]]

if __name__ == "__main__":
    # Example test cases
    print(make_ends([1, 2, 3]))  # Output: [1, 3]
    print(make_ends([1, 2, 3, 4]))  # Output: [1, 4]
    print(make_ends([7, 4, 6, 2]))  # Output: [7, 2]
    print(make_ends([1, 2, 2, 2, 2, 2, 2, 3]))  # Output: [1, 3]
    print(make_ends([7, 4]))  # Output: [7, 4]
    print(make_ends([7]))  # Output: [7, 7]
    print(make_ends([5, 2, 9]))  # Output: [5, 9]
    print(make_ends([2, 3, 4, 1]))  # Output: [2, 1]
