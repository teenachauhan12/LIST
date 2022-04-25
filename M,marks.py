marks=[
    [78,76,94,86,88],
    [91,71,98,65,76],
    [95,45,78,52,49]
]
a=[]
i=0
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        sum+=marks[i][j]
        j+=1
    a.append(sum)
    i+=1
print(a)