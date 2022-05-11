n = int(input("Digite a quantidade de numeros que serao inseridas"))
l = []
i = 0
while i < n:
    l.append(int(input("Digite um valor")))
    i = i + 1
primos = []
num = 2
while num <= 30:
    mult = 0
    for count in range(2,num):
        if (num % count == 0):
            mult += 1
    if(mult == 0):
        primos.append(num)
    num += 1
cNum = set(l)
cPrimos = set(primos)
print("Numeros digitados que são primos: "+str(cNum.intersection(cPrimos)))
