# Version 1
def makes10(a, b):
    return (a == 10 or b == 10 or a + b == 10)

# # Version 2
# def makes10(a, b):
#     if a == 10 or b == 10 or a + b == 10:
#         return True
#     else:
#         return False

if __name__ == "__main__":
    makes10(9, 10)  #True
    makes10(9, 9)  #False
    makes10(1, 9)  #True