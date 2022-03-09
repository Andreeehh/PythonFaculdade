h = int(input("Digite a quantidade de horas"))
m = int(input("Digite a quantidade de minutos"))
s = int(input("Digite a quantidade de segundos"))
if h <10:
    hStr ="0" + str(h)
else:
    hStr = str(h)
if m <10:
    mStr ="0" + str(m)
else:
    mStr = str(m)
if s <10:
    sStr ="0" + str(s)
else:
    sStr = str(s)
print("Formato original: "+hStr+":"+mStr+":"+sStr)
s = (h*60*60) + (m*60) + s
print("Em segundos: " + str(s)+ " segundos")