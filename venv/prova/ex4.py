v1 = []
v2 = []
v3 = []
for i in range(5):
    v1.append(int(input("Digite um numero para lista 1")))
    v2.append(int(input("Digite um numero para lista 2")))
    v3.append(v1[i] * v2[i])
print("Lista 1: " + str(v1))
print("Lista 2: " + str(v2))
print("Lista 3: " + str(v3))