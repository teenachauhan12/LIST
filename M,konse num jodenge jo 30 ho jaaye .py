number=30
n=[12,14,18,16,13,10,11,19]
i=0
a=[]
while i<len(n):
    j=0
    while j<len(n):
        b=n[i]+n[j]
        if number==b:
            c=[n[i],n[j]]
            a.append(c)
        j+=1
    i+=1
print(a)