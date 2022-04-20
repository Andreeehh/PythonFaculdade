def maxList(listas):
    listMax = []
    i = 0
    while i < len(listas):
        listMax.append(max(listas[i]))
        i += 1
    return listMax
listas = [[1,2],[30,4],[5,6]]
print(maxList(listas))