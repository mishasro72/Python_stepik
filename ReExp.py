import re

# def low_case(s):
#     return len(re.findall('[a-z]', s))

# def fined(s):
#     return(re.findall('he..o', s))

# def fined_start(s):
#     return(re.findall(r'\Bel|lo\B', s))

# print(low_case('hHHHSJAHSHnn'))
# print(fined('hello everybody bello'))
# print(fined_start('hello everybody hello'))


# txt = "The rain in Spain"
# x = re.search(r"ai", txt)
# print(x.span())

# x = re.search(r'lo', 'hello everubody')
# print(x.span())
# print(x.string)
# print(x.group())

# def validate_usr(username):
#     if 4 <= len(username) <= 16:
#         if re.findall('\W', username):
#             return False
#         else:
#             if re.findall('[A-Z]', username):
#                 return False
#             else:  
#                 return True
#     else:
#         return False

# print(validate_usr('pitter'))

def validate_usr(username):
    return bool(re.match(r'^[a-z0-9_]{4,16}$', username))

print(validate_usr('piter+'))

# import re

# #Check if the string starts with "The" and ends with "Spain":

# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x.span())

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")
