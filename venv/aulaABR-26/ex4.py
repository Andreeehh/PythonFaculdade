p1 = input("Digite a primeira palavra")
p2 = input("Digite a segunda palavra")
l1 = list(p1)
l2 = list(p2)
l1.sort()
l2.sort()
if l1 == l2:
    print("Anagramas")
else:
    print("Não anagrama")