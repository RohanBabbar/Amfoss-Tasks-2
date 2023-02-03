import re
a = input("enter password ")
def password(a):
    passwordRegex = re.compile(r'[a-z]')
    new = passwordRegex.findall(a)
    passwordRegex = re.compile(r'[A-Z]')
    new3 = passwordRegex.findall(a)
    passwordRegex = re.compile(r'[0-9]')
    new2 = passwordRegex.findall(a)
    big = new+new3
    # pattern = '[A-Z]'
    # b = '[a-z]'
    # if re.search(pattern, a):
    #     return('Yes')
    # else:
        # return('No')
    if len(big)>=8:
        if len(new2)>=1 and len(new3)>0:
            print("Strong Password")
        else:
            print("Nope")
    else:
        print("Not so strong")
    print(new)
    # print(new3)
    # print(big)
password(a)
# if len(new)>=8:
#     if new.isupper():
#         print("True")