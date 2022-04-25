
# a=[1,2,3,4,5,6]
# # # output=[1,10,2,20,3,10,4,20,5,10,6,20]
# i=0
# b=[]
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#         b.append(20)
#     else:
#         b.append(a[i])
#         b.append(10)
#     i+=1
# print(b)




# a=[[2,4,3],8,[9,3,7],9,[2,4,3]]
# i=0
# while i<len(a):
#     if type(a[i])!=list:
#         a[i-1].append(a[i])
#         a.remove(a[i])
#     else:
#         pass
#     i+=1j
# print(a)





# # a=[1,2,0,5,0,7,0,1]
# # output=[1,2,5,7,1,0,0,0]


# a=[1,2,0,5,0,7,0,1]
# i=0
# b=[]
# while i<len(a):
#     if a[i]==0:
#         pass
#     else:
#         b.append(a[i])
#     i+=1
# i=0
# while i<len(a):
#     if a[i]!=0:
#         pass
#     else:
#         b.append(a[i])
#     i+=1
# print(b)




# num=int(input("enter the num"))
# a=num%10
# if a==3:
#     print("its display")
# else:
#     print("not display")

    


# a=[[10,20,30],[40,50,60]]
# print(a[0][0])
# print(a[0][1])
# print(a[0][2])
# print(a[1][1])
# print(a[1][2])
# print(a)
# i=0
# b=[]
# while i<len(a):
#     b+=a[i]
#     i+=1
# print(b)


# a=[2,3,5,12,7,8,10]
# b=[]
# i=0
# while i<len(a):
#     if a[i]%2==0:
#         b.append(a[i])
#     i+=1
# print(b)




# a=["44413","13(1)","40EE"]
# i=0
# b=[]
# while i<len(a):
#     e=''
#     j=0
#     while j<2:
#         e+=a[i][j]
#         j+=1
#     b.append(e)
#     i+=1
# print(a)
# print(b)



# a=[[2,3],5,4,[[7,8],9],10]
# print(a[0][0])
# print(a[0][1])
# print(a[1])
# print(a[2])
# print(a[3][0][0])
# print(a[3][0][1])
# print(a[3][1])
# print(a[4])
# print(a[5])



# a=["teena"]
# i=0
# c=0
# while i<len(a[0]):
#     c=c+1
#     print(a[0][-c],end="")
#     i+=1




# a=["python","hello","teena"]
# i=0
# max=0
# while i<len(a):
#     if len(a[i])>max:
#         max=len(a[i])
#         l=a[i]
#     i+=1
# print(l)





# a=int(input("enter the numer"))
# i=1
# c=[]
# while i<=10:
#     d=(a*i)
#     c.append(d)
#     i=i+1
# print(c)




# list1=["m","na","i","tee"]
# list2=["y","me","s","na"]
# i=0
# b=[]
# while i<len(list1):
#     print(list1[i]+list2[i],end=" ")
#     i+=1



a=[1,3,5,7,9]
a[3]=2
a[2]=4
print(a)






















