s = float(input("Digite o salário:\n"))
v = float(input("Digite as vendas do funcionário:\n"))
if v >= 1000 and v <=5000:
    s = s + 500
elif v > 5000 and v <= 7500:
    s = s + 750
elif v > 7500:
    s = s + 1000
print("Salário final = " + str(s))