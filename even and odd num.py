n=[9,1,8,2,7,3,6,4,5,24,12]
i=0
while i<len(n):
    if n[i]%2==0:
        print(n[i],"even")
    else:
        print(n[i],"odd")
    i+=1