v = [0, 50, 23, 31, 78]
n = int(input("Digite o valor a ser procurado"))
x = -1
for i in range(len(v)):
    if n == v[i]:
        x = i
print("Indice: " + str(x))
#talon
j = 0
while j < 5 and n != v[j]:
    j = j + 1
if j == 5:
    print(-1)
else:
    print(j)