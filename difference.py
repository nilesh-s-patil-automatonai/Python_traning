l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
l3=[]
for x in l1:
        if x not in l2:
            l3.append(x)
for x in l2:
        if x not in l1:
            l3.append(x)

print(l3)
