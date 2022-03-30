list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
list2 =  [list1[19]] + list1[0:-1]
list3 =  list1[1:] + [list1[0]]
print(list1)
print(list2)
print(list3)