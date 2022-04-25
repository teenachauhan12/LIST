a=[6,2,3,8]
min=a[0]
max=a[0]
for i in a:
    if i>max:
        max=i
    if i<min:
        min=i
b=[]
for s in range(min,(max+1)):
    b.append(s)
    print(s)
c=[]
z=0
d=0
while z<len(b):
    if b[z]not in a:
        c.append(b[z])
        d+=1
    z+=1
print(c,d)
 
