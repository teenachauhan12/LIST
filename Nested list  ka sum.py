a=[1,2,2,[1,2,3,[3,4,5]]]
sum=0
i=0
while i<len(a):
    if type (a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    sum+=a[i][j][k]
                    k+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
         sum+=a[i]
    i+=1
print(sum)






a=[1,2,[6,7],[3,4,[8,4,[2,5],[0,1]]]]
sum=0
i=0
while i<len(a):
    if type(a[i])==list:
        j=0
        while j<len(a[i]):
            if type(a[i][j])==list:
                k=0
                while k<len(a[i][j]):
                    if type(a[i][j][k])==list:
                        m=0
                        while m<len(a[i][j][k]):
                            sum+=a[i][j][k][m]
                            m+=1
                    else:
                        sum+=a[i][j][k]
                    k+=1
            else:
                sum+=a[i][j]
            j+=1
    else:
        sum+=a[i]
    i+=1
print(sum)




