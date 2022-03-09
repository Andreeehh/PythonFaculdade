n1 = int(input("Digite o 1º numero"))
n2 = int(input("Digite o 2º numero"))
n3 = int(input("Digite o 3º numero"))
if n1 > 0 and n2 > 0 and n3 > 0:
    area = ((n1+n2)/2) * n3
    print("Valor da área de " + str(area))
else:
    print("Existe algum valor negativo")