kitna=[3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100]
i=0
count=0
counter=0
countent=0
while i<len(kitna):
    if kitna[i]>100000 and kitna[i]<10000000:
        count=count+1
    elif kitna[i]<100000:
        counter=counter+1
    else:
        countent=countent+1
    i+=1
print("karodpati",counter)
print("lakpati",count)
print("dilwale",countent)