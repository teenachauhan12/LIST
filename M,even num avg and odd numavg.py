# element=[23,14,56,12,19,9,4,15,25,31,42,43]
# i=0
# sum=0
# count=0
# sum1=0
# count1=0
# while i<len(element):
#     a=element[i]
#     if a%2==0:
#         sum+=element[i]
#         count=count+1
#     i+=1
# print(sum,count,"avrage=",sum//count)
# print(sum1,count1,"avrage=",sum1//count1)






elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c1=0
sum=0
sum1=0
while i<len(elements):
    if elements[i]%2==0:
        sum+=elements[i]
        c+=1
    else:
        sum1+=elements[i]
        c1+=1
    i+=1
print("count of even=",c)
print("count of odd=",c1)
print("count all numbers=",len(elements))
print("sum of even=",sum)
print("sum of odd=",sum1)
print("sum of all=",sum+sum1)
print("avg of even=",sum/c)
print("avg of odd=",sum1/c1)
print("avg of all=",(sum+sum1)/len(elements))


