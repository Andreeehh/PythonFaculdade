l1 = int(input("L1:"))
l2 = int(input("L2:"))
l3 = int(input("L3:"))
abs1 = abs(l2-l3)
abs2 = abs(l1-l3)
abs3 = abs(l1-l2)
s1 = l2+l3
s2 = l1+l3
s3 = l2+l1
if abs1 < l1 and l1 < s1 and abs2 < l2 and l2 < s2 and abs3 < l3 and l3 < s3:
    print("Forma um triangulo")
else:
    print("Não forma um triangulo")