def add(a,b):
    c=a+b
    print(c)
def sub(a,b):
    c=a-b
    print(c)
def mul(a,b):
    c=a*b
    print(c)
def div(a,b):
    c=a/b
    print(c)
def main():
    a=input(eval("enter 1st no"))
    b=input(eval("enter 2nd no"))
    return add(a,b)
    return sub(a,b)
    return mul(a,b)
    return div(a,b)
def menu():
    print("Welacome","\n Your options are")
    print("1 addition")
    print("2 subtraction")
    print("3 multiplication")
    print("4 division")
    print("5 exit")
    ch= input("choose your option")
    ch=menu()
    if ch=='0':
        print("you enter wrong choice")
    elif ch== '1':
        print(add())
    elif ch == '2':
        print(sub())
    elif ch == '3':
        print(mul())
    elif ch== '4':
        print(div())
    elif ch>'5':
        exit()