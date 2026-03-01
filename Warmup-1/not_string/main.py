# Version 1:
def not_string(str):
    if str.startswith('not'):
        return str
    else:
        return 'not ' + str

# # Version 2:
# def not_string(str):
#     if str[:3] == 'not':
#         return str
#     else:
#         return 'not ' + str

if __name__ == "__main__":
    print(not_string('candy'))  #'not candy'
    print(not_string('x'))  #'not x'
    print(not_string('not bad')) #'not bad'
