a=[1,2,3,[3,4],[6,7,8,[9,1,2]]]
s=str(a)
i=0
c=0
while i<len(s):
    if s[i]=="[":
        c+=1
    i+=1
print(c)


