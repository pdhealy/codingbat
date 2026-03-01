# Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.

# Version 1 (My Attempt)
def common_end(a, b):
    if len(a) <= 1 and len(b) <= 1:
        return False

    return (a[0] == b[0]) or (a[len(a)-1] == b[len(b)-1])

# Version 2 (Optimized)
def common_end(a, b):
    return (a[0] == b[0]) or (a[-1] == b[-1])

if __name__ == "__main__":
    # Example test case
    print(common_end([1, 2, 3], [7, 3]))  # Output: True
    print(common_end([1, 2, 3], [7, 3, 2]))  # Output: False
    print(common_end([1, 2, 3], [1, 3]))  # Output: True
    print(common_end([1, 2, 3], [1]))  # Output: True
    print(common_end([1, 2, 3], [2]))  # Output: False