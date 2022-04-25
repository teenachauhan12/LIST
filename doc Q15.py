list1=['Python', 'list', 'exercises', 'practice', 'solution']
import random
b=[]
for i in list1:
    a=list(i)
    random.shuffle(a)
    a="".join(a)
    b.append(a)
print(b)
