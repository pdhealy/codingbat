# Version 1
def pos_neg(a, b, negative):
    # Start with the invariant that if negative is True, then both a and b must be negative
    if negative:
        return (a < 0 and b < 0)
    else:
        return ((a < 0 and b > 0) or (a > 0 and b < 0))

# # Version 2: My attempt
# def pos_neg(a, b, negative):
#     if negative:
#         if a < 0 and b < 0:
#             return True
#         else:
#             return False
#     elif a < 0 and b >= 0:
#         return True
#     elif b < 0 and a >= 0:
#         return True
#     else:
#         return False

if __name__ == "__main__":
    print(pos_neg(1, -1, False))  #True
    print(pos_neg(-1, 1, False))  #True
    print(pos_neg(-4, -5, True))  #True