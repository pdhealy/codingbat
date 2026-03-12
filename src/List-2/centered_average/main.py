# Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

# Version 1 (My Attempt - was on the right track but required AI assistance to complete)
def centered_average(nums):
    array = {}

    for num in nums:
        if num in array:
            array[num] += 1
        else:
            array[num] = 1

    if min(array.keys()) in array:
        array[min(array.keys())] -= 1
        if array[min(array.keys())] == 0:
            del array[min(array.keys())]

    if max(array.keys()) in array:
        array[max(array.keys())] -= 1
        if array[max(array.keys())] == 0:
            del array[max(array.keys())]

    return sum(array.keys()) // len(array.keys())

    if max(array[num]) >= 1:
        array[num] -1

    return sum(array[num]) / len(array[num])

# Version 2 (Solution)
def centered_average(nums):
    nums.sort()
    return sum(nums[1:-1]) // (len(nums) - 2)

# Version 3 (Optimized)
def centered_average(nums):
    min_val = min(nums)
    max_val = max(nums)
    nums.remove(min_val)
    nums.remove(max_val)
    return sum(nums) // len(nums)

if __name__ == "__main__":
    # Example test cases
    print(centered_average([1, 2, 3, 4, 100]))  # Output: 3
    print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # Output: 5
    print(centered_average([-10, -4, -2, -4, -2, 0]))  # Output: -3
    print(centered_average([5, 3, 4, 6, 2]))  # Output: 4
    print(centered_average([5, 3, 4, 0, 100]))  # Output: 4
    print(centered_average([100, 0, 5, 3, 4]))  # Output: 4
    print(centered_average([4, 0, 100]))  # Output: 4
    print(centered_average([0, 2, 3, 4, 100]))  # Output: 3
    print(centered_average([1, 1, 100]))  # Output: 1
    print(centered_average([7, 7, 7]))  # Output: 7
    print(centered_average([1, 7, 8]))  # Output: 7
    print(centered_average([1, 1, 99, 99]))  # Output: 50
    print(centered_average([1000, 0, 1, 99]))  # Output: 50
    print(centered_average([4, 4, 4, 4, 5]))  # Output: 4
    print(centered_average([4, 4, 4, 1, 5]))  # Output: 4
    print(centered_average([6, 4, 8, 12, 3]))  # Output: 6