p = float(input("Digite o peso em kg"))
a = float(input("Digite a altura em m"))
imc = p / (a*a)
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("normal")
elif imc < 30:
    print("Acima do peso")
else:
    print("Obeso")