import random
list = []
for i in range(1, 11):
    list = list + random.sample(range(1,10), k=1)
count = 0
sorteado = 0
for i in range(1, 11):
    if(list.count(i)> count):
        count = list.count(i)
        sorteado = i
print(list)
print(sorteado)