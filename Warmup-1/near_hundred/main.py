# Version 1
def near_hundred(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

# Version 2
def near_hundred(n):
    # Uses extra brackets
    return (abs(n - 100) <= 10) or (abs(n - 200) <= 10)

# Version 3
def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return False

if __name__ == "__main__":
    near_hundred(93)  #True
    near_hundred(90)  #True
    near_hundred(89)  #False
    near_hundred(110)  #True
    near_hundred(111)  #False
    near_hundred(121)  #False
    near_hundred(-101)  #False
    near_hundred(-209)  #False
    near_hundred(190)  #True
    near_hundred(209)  #True
    near_hundred(0)  #False
    near_hundred(5)  #False
    near_hundred(-50)  #False
    near_hundred(191)  #True
    near_hundred(189)  #False
    near_hundred(200)  #True
    near_hundred(210)  #True
    near_hundred(211)  #False
    near_hundred(290)  #False
