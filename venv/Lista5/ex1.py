import math
def calcRaizes(a, b, c):
    delta = b**2 - (4*a*c)
    x1 = (((-1) * b) + (delta ** 0.5)) / (2 * a)
    x2 = (((-1) * b) - (delta ** 0.5)) / (2 * a)
    if (delta < 0):
        return "Delta negativo, sem raizes reais"
    elif (delta == 0):
        return "Delta igual a 0, apenas uma raiz real de valor " + str(x1)
    else:
        return "Delta maior que 0, raiz real 1 de valor " + str(x1) + " raiz real 2 de valor " + str(x2)
print(calcRaizes(1,5,6))