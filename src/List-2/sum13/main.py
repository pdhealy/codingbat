# Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

# Version 1 (My Attempt - using a for loop and break statement - not working)
def sum13(nums):
    array = []

    for num in nums:
        if num == 13:
            break
        else:
            array.append(num)

    if array:
        return sum(array)
    else:
        return 0

# Version 2 (My 2nd Attempt - working, but overcomplicated)
def sum13(nums):
    array = []
    index = 1

    while index < (len(nums) + 1):
        if nums[index - 1] == 13:
            index += 2
        else:
            array.append(nums[index - 1])
            index += 1
    
    if array:
        return sum(array)
    else:
        return 0

# Version 3 (Solution from CodingBat)
def sum13(nums):
    sum = 0
    i = 0

    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            sum += nums[i]
            i += 1

    return sum

# Version 4 (Codex Solution - using a for loop and a flag to skip the next number after 13)
def sum13(nums):
    total = 0
    skip_next = False

    for num in nums:
        if num == 13:
            skip_next = True
        elif skip_next:
            skip_next = False
        else:
            total += num

    return total

if __name__ == "__main__":
    # Example test cases
    print(sum13([1, 2, 13, 2, 1, 13]))
    print(sum13([13, 1, 2, 13, 2, 1, 13]))
