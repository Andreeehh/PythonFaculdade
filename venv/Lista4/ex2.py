import random

list = []
for i in range(10):
    list = list + random.sample(range(1, 10), k=1)
avg = sum(list) / len(list)
maiores = []
menores = []
for i in range(10):
    if (list[i] >= avg):
        maiores.append(list[i])
    else:
        menores.append(list[i])
print(avg)
print(list)
print(maiores)
print(menores)
print("Quantidade de maiores = " + str(len(maiores)))
print("Quantidade de menores = " + str(len(menores)))
