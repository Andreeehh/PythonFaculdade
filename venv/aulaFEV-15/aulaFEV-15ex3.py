import math
ponto1x = int(input("Digite o eixo x do primeiro ponto"))
ponto1y = int(input("Digite o eixo y do primeiro ponto"))
ponto2x = int(input("Digite o eixo x do segundo ponto"))
ponto2y = int(input("Digite o eixo y do segundo ponto"))
d = math.sqrt((ponto2x-ponto1x)**2 + (ponto2y-ponto1y)**2)
print("Distancia entre os pontos de: " + str(d))