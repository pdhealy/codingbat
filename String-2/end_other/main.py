# Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

# Version 1 (My Attempt)
# Incorrect behavior when either input is empty due to -0 slicing edge case.
def end_other(a, b):
    min_val = min(len(a), len(b)) * -1
    return a[min_val:].lower() == b[min_val:].lower()


# Version 2 (Solution)
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a.endswith(b) or b.endswith(a)


# Version 3 (Alternative Solution)
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return a[-len(b) :] == b or b[-len(a) :] == a


if __name__ == "__main__":
    # Example test cases
    print(end_other("Hiabc", "abc"))  # Output: True
    print(end_other("AbC", "HiaBc"))  # Output: True
    print(end_other("abc", "abXabc"))  # Output: True
    print(end_other("Hiabc", "abcd"))  # Output: False
    print(end_other("Hiabc", "bc"))  # Output: True
    print(end_other("Hiabcx", "bc"))  # Output: False
    print(end_other("abc", "abc"))  # Output: True
    print(end_other("xyz", "12xyz"))  # Output: True
    print(end_other("yz", "12xz"))  # Output: False
    print(end_other("Z", "12xz"))  # Output: True
    print(end_other("12", "12"))  # Output: True
    print(end_other("abcXYZ", "abcDEF"))  # Output: False
    print(end_other("ab", "ab12"))  # Output: False
    print(end_other("ab", "12ab"))  # Output: True
