# n=[0,9,5]
# i=0
# while i<len(n):
#     j=0
#     while j<len(n):
#         k=0
#         while k<len(n):
#             if i!=j and j!=k and i!=k:
#                 print(n[i],n[j],n[k])
#             k+=1
#         j+=1
#     i+=1








a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

    