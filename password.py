import re
passw=input("Enter Password")
flag=0
if (len(passw) < 8 or  len(passw)>15):
     print("password must be between 8 to 15 char")
     flag=-1

elif not re.search("[a-z]", passw):
    flag= -1
    print("password must contain atlist 1 small char")

elif not re.search("[A-Z]", passw):
        flag = -1
        print("password must contain atlist 1 capital char")
elif not re.search("[0-9]", passw):
        flag = -1
        print("password must contain atlist 1 number")

elif not re.search("[_@$!#]", passw):
        flag = -1
        print("password must contain atlist 1 special character")

elif  re.search("[.]", passw):
        flag = -1
        print(". is not valid")

else:
    flag = 0
    print("Valid Password")


if flag == -1:
    print("Password is not valid")