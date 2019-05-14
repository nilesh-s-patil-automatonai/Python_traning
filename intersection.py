l1=[1,2,3,4]
l2=[3,4,5,6,7]
l3=[]
for x in l1:
    if x in l2:
        l3.append(x)
print(l3)
