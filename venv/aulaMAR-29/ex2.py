list1 = [1, 4, 5]
list2 = [3, 8, 9]
print ("Original list 1 : " + str(list1))
print ("Original list 2 : " + str(list2))
res = []
for i in range (3):
    res = res + [list1[i]] + [list2[i]]
print ("Lista intercalada : " + str(res))