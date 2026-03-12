# Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.

# Version 1 (My Attempt)
def middle_way(a, b):
    return [a[1], b[1]]

# Version 2 (My Second Attempt)
def middle_way(a, b):
    if len(a) ==  len(b):
        if len(a) % 2 == 1:
            middle = (len(a) // 2)
            return [a[middle], b[middle]]

# Version 3 (Optimized)
def middle_way(a, b):
    return [a[len(a) // 2], b[len(b) // 2]]


# Version 4 (Using a `while` loop)
def middle_way(a, b):
    middle = 0
    while middle < len(a) and middle < len(b):
        if middle == len(a) // 2:
            return [a[middle], b[middle]]
        middle += 1

if __name__ == "__main__":
    # Example test cases
    print(middle_way([1, 2, 3], [4, 5, 6]))  # Output: [2, 5]
    print(middle_way([7, 7, 7], [3, 8, 0]))  # Output: [7, 8]
    print(middle_way([5, 2, 9], [1, 4, 5]))  # Output: [2, 4]
    print(middle_way([1, 9, 7], [4, 8, 8]))  # Output: [9, 8]
    print(middle_way([1, 2, 3], [3, 1, 4]))  # Output: [2, 1]
    print(middle_way([1, 2, 3], [4, 1, 1]))  # Output: [2, 1]
