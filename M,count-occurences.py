
char_list = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
c=0
c1=0
c2=0
c3=0
c4=0
c5=0
while i<len(char_list):
    if "a" in char_list[i]:
        c+=1
    elif "n" in char_list[i]:
        c1+=1
    elif "t" in char_list[i]:
        c2+=1
    elif "x" in char_list[i]:
        c3+=1
    elif "u" in char_list[i]:
        c4+=1
    else:
        c5+=1
    i+=1
print("a-",c,'time')
print("n-",c1,'time')
print("t-",c2,'time')
print("x-",c3,'time')
print("u-",c4,'time')
print("g-",c5,'time')
print([["a", 6], ["n", 3], ["t", 2], ["x", 2], ["u", 1], ["g", 1]])