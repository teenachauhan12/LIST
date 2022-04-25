a=[12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
i=0
k=0
list=[]
while i<len(a):
    b=[]
    j=0
    while j<3 and k!=len(a):
        b.append(a[k])
        k+=1
        j+=1
    list.append(b)
    if k==len(a):
        break
    i+=1
print(list)

