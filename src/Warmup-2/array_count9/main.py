# Version 1 (My Attempt): (working)
def array_count9(nums):
    count = 0

    for num in nums:
        if num == 9:
            count += 1

    return count

if __name__ == "__main__":
    # Example test cases
    print(array_count9([1, 2, 9]))  # Output: 1
    print(array_count9([1, 9, 9]))  # Output: 2
    print(array_count9([1, 9, 9, 3, 9]))  # Output: 3
    print(array_count9([1, 2, 3]))  # Output: 0
    print(array_count9([]))  # Output: 0
    print(array_count9([4, 2, 4, 3, 1]))  # Output: 0
    print(array_count9([9, 2, 4, 3, 1]))  # Output: 1
