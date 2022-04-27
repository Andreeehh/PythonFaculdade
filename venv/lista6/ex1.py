vogais = ["a","e","i","o","u"]
frase = input("Digite uma frase")
count = 0
for x in range(0,5):
    count += frase.count(vogais[x])
print(count)