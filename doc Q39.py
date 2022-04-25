
a=[[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
i=0
s=0
while i<len(a):
    j=0
    while j<len(a):
        if len(a[i])<len(a[j]):
            a[i].append(0)
        j+=1
    i+=1
b=0
c=0
while c<5:
    h=a[0][b]+a[1][b]+a[2][b]+a[3][b]+a[4][b]
    c+=1
    b+=1
    print(h/len(a))