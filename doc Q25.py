test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
L = []
for i in test_list:
    if i not in L:
        if test_list.count(i) > 3:
            L.append(i)
print(L)

