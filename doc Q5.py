
n = [1, 2, 2, 5, 8, 4,8]
i=0
a=[]
count=0
while i<len(n):
    j=n[i]
    if j not in a:
        a.append(j)
        count=count+1
    i+=1
print(a)
print(count)
