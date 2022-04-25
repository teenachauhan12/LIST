n=int(input('enter the num'))
r=0
i=0
while n>0:
    r=n%10
    i=i*10+r
    n=n//10
print("reverse num is",i)
