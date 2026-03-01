# Version 1:
def missing_char(str, n):
    front = str[:n]  # up to but not including n
    back = str[n + 1:]  # n+1 (including n+1)through end of string
    return front + back

# # Version 2: My attempt
# def missing_char(str, n):
#     new_str = []
#     for index in range(len(str)):
#         if index != n:
#            new_str.append(str[index])
#     return ''.join(new_str)

if __name__ == "__main__":
    print(missing_char('kitten', 1))  # Output: 'ktten'
    print(missing_char('kitten', 0))  # Output: 'itten'
    print(missing_char('kitten', 4))  # Output: 'kittn'
