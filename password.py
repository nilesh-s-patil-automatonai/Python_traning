import re
passw=input("Enter Password")

flag = 0
while True:
    if (len(passw) < 8 or  len(passw)>15):
        flag = -1
        print("password must be between 8 to 15 char")
        break
    elif not re.search("[a-z]", passw):
        flag = -1
        print("password must contain atlist 1 small char")
        break
    elif not re.search("[A-Z]", passw):
        flag = -1
        print("password must contain atlist 1 capital char")
        break
    elif not re.search("[0-9]", passw):
        flag = -1
        print("password must contain atlist 1 number")
        break
    elif not re.search("[_@$!#]", passw):
        flag = -1
        print("password must contain atlist 1 special character")
        break
    elif  re.search("[.]", passw):
        flag = -1
        print(". is not valid")
        break

    else:
        flag = 0
        print("Valid Password")
        break

if flag == -1:
    print("Password is not valid")