a = int(input("Digite A:\n"))
b = int(input("Digite B:\n"))
quociente = 0
resto = 0
while a - b > 0:
    if(a - b > 0):
        quociente = quociente + 1
    a = a - b
resto = a
print("Quociente = " + str(quociente))
print("Resto = " + str(resto))