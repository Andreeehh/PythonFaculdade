l1 = [1, 3, 5, 7, 8, 10, 9, 2, 11, 20]
l2 = [4, 8, 9, 10, 20, 3, 5, 7, 2, 1]
c1 = set(l1)
c2 = set(l2)
c = len(c1.difference(c2)) + len(c2.difference(c1))
print("quantidade de numeros diferentes " + str(c))
