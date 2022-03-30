v1 = [0, 1, 6, 3, 3, 4, 5, 1 ,7, 7]
c = len(v1)
i = 0
v2 = []
dif = []
for x in range(10):
    v2.append(v1[x])
while i < len(v1):
    v2.remove(v1[i])
    if v1[i] in v2:
        c = c - 1
    i = i + 1
print(str(c))
#talon
for j in range(10):
    if v1[j] not in dif:
        dif.append(v1[j])
print("Dif" + str(dif))
print(len(dif))