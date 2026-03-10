# Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.

# Version 1 (My Attempt - not working correctly)
def xyz_there(str):
    for index in range(1, len(str) - 1):
        if str[index - 1] == ".":
            # index += 2 inside a for loop does not skip future loop iterations.
            index += 2

        if str[index - 1 : index + 2] == "xyz":
            return True

    return False


# Version 2 (Optimized)
def xyz_there(str):
    for index in range(len(str) - 2):
        if str[index : index + 3] == "xyz" and (index == 0 or str[index - 1] != "."):
            return True

    return False

# Version 3 (Using while loop)
def xyz_there(str):
    index = 0
    
    while index <= len(str) - 3:
        if str[index - 1] == '.' and index > 0:
            index += 1
            continue
        
        if str[index:index + 3] == 'xyz':
            return True
        
        index += 1
    
    return False


if __name__ == "__main__":
    # Example test cases
    print(xyz_there("abcxyz"))  # Output: True
    print(xyz_there("abc.xyz"))  # Output: False
    print(xyz_there("xyz.abc"))  # Output: True
    print(xyz_there("abcxy"))  # Output: False
    print(xyz_there("xyz"))  # Output: True
    print(xyz_there("xy"))  # Output: False
    print(xyz_there("x"))  # Output: False
    print(xyz_there(""))  # Output: False
    print(xyz_there("abc.xyzxyz"))  # Output: True
    print(xyz_there("abc.xxyz"))  # Output: True
    print(xyz_there(".xyz"))  # Output: False
    print(xyz_there("12.xyz"))  # Output: False
    print(xyz_there("12xyz"))  # Output: True
    print(xyz_there("1.xyz.xyz2.xyz"))  # Output: False
