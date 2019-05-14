l1=[1,2,3,4]
l2=[3,4,5,6,7]
l3=l1
for x in l2:
    if x not in l1:
        l3.append(x)
print(l3)
