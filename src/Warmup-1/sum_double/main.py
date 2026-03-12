def sum_double(a, b):
    sum = a + b

    if a == b:
        sum = sum * 2
    return sum

if __name__ == "__main__":
    print(sum_double(1,2))  #3
    print(sum_double(3,2))  #5
    print(sum_double(2,2))  #8
