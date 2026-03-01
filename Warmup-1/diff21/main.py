# Version 1 (using abs())
def diff21(n):
    # Good approach - places the exception first and then the normal case.
    if n > 21:
        return abs(n - 21) * 2
    else:
        return abs(n - 21)

# Version 2
# def diff21(n):
#    if n <= 21:
#        return 21 - n
#    else:
#        # Handles the exception seperately
#        return (n - 21) * 2

# Original version
# def diff21(n):
#   # Calculate difference and store in variable
#   diff = abs(21 - n)
  
#   # If n is greater than 21 multiply diff by 2
#   if n > 21:
#     diff = diff * 2
  
#   # Return diff
#   return diff

if __name__ == "__main__":
    diff21(19)  #2
    diff21(10)  #11
    diff21(21)  #0