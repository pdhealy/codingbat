# Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.

# Version 1 (My Attempt)
def reverse3(nums):
    return nums[::-1]

# Version 2 (My Second Attempt)
def reverse3(nums):
    output = []

    for index in range(len(nums) - 1, -1, -1): # What does this mean?
        output.append(nums[index])

    return output

# Version 3 (Optimized)
def reverse3(nums):
    return [nums[2], nums[1], nums[0]]

# Version 4 (Using a while and for loop)
def reverse3(nums):
    output = []
    index = len(nums) - 1

    while index >= 0:
        output.append(nums[index])
        index -= 1

    return output

if __name__ == "__main__":
    # Example test cases
    print(reverse3([1, 2, 3]))  # Output: [3, 2, 1]
    print(reverse3([5, 11, 9]))  # Output: [9, 11, 5]
    print(reverse3([7, 0, 0]))  # Output: [0, 0, 7]
    print(reverse3([2, 1, 2]))  # Output: [2, 1, 2]
    print(reverse3([1, 2, 1]))  # Output: [1, 2, 1]
    print(reverse3([2, 11, 3]))  # Output: [3, 11, 2]
    print(reverse3([0, 6, 5]))  # Output: [5, 6, 0]
    print(reverse3([7, 2, 3]))  # Output: [3, 2, 7]
