# a=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while i<(len(a)-1):
#     b=a[i+1]-a[i]
#     print(b,end="")
#     i+=1




# a=[2,4,6,8]
# i=0
# while i<(len(a)-1):
#     b=a[i+1]-a[i]
#     print(b,end="")
#     i+=1


a=[1,2,3,4,5,6,7,8,9]
i=0
while i<len(a):
    if a[i]%2!=0:
        print(a[i],"odd num")
    i+=1
    