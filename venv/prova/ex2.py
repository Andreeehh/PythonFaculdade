v = float(input("Valor da venda sem desconto: "))
t = int(input("Tipo de desconto:\n0 - Valor fixo\n1 - Porcentagem\n"))
d = float(input("Valor do desconto"))
if t == 1:
    vf = v - (v * d / 100)
elif t == 0:
    vf = v - d
else:
    print("Tipo incorreto")
print("Valor da venda com desconto: " + str(vf))