vogais = ["a","e","i","o","u"]
frase = input("Digite uma frase")
for x in range(0,5):
    frase = frase.replace(vogais[x],"")
print(frase)