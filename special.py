sum=0
num=int(input("Enter a number:"))
temp=num
while(num):
    i=1
    f=1
    r=num%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    num=num//10
if(sum1==temp):
    print("The number is a special number")
else:
    print("The number is not a special number")
