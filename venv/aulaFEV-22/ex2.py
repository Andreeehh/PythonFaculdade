id1 = int(input("Digite o código do cliente 1 "))
v1 = float(input("Digite o valor pago pelo cliente 1 "))
id2 = int(input("Digite o código do cliente 2 "))
v2 = float(input("Digite o valor pago pelo cliente 2 "))
id3 = int(input("Digite o código do cliente 3 "))
v3 = float(input("Digite o valor pago pelo cliente 3 "))
m = (v1 + v2 + v3) / 3
menor = 0
maior = 0
if v1 > m:
    maior += 1
else:
    menor += 1
if v2 > m:
    maior += 1
else:
    menor += 1
if v3 > m:
    maior += 1
else:
    menor += 1
print("Quantidade de clientes que pagaram um valor maior que a média: " + str(maior))
print("Quantidade de clientes que pagaram um valor menor que a média: " + str(menor))