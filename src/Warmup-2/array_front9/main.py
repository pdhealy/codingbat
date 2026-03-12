# Version 1 (My Attempt): (working)
# Using a ``while loop
def array_front9(sums):
    i = 0
    while i < len(sums) and i < 4:
        if sums[i] == 9:
            return True
        i += 1
    return False

# Version 2 (My Attempt): (working)
# Using a `for`` loop
def array_front9(sums):
    for num in sums[:4]:
        if num == 9:
            return True
    return False

if __name__ == "__main__":
    # Example test cases
    print(array_front9([1, 2, 9, 3, 4]))  # Output: True
    print(array_front9([1, 2, 3, 4, 9]))  # Output: False
    print(array_front9([1, 2, 3, 4, 5]))  # Output: False
    print(array_front9([9, 2, 3]))  # Output: True
    print(array_front9([1, 9, 9]))  # Output: True
    print(array_front9([1, 2, 3]))  # Output: False
    print(array_front9([1, 9]))  # Output: True
    print(array_front9([5, 5]))  # Output: False
    print(array_front9([2]))  # Output: False
    print(array_front9([9]))  # Output: True
    print(array_front9([]))  # Output: False
    print(array_front9([3, 9, 2, 3, 3]))  # Output: True
