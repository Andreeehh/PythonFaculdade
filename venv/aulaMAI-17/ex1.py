frase = input("Digite uma frase")
vogais = {"a": [frase.count("a")], "e": [frase.count("e")], "i": [frase.count("i")], "o": [frase.count("o")]
          ,"u": [frase.count("u")]}
print("Quantidade de a = " + str(vogais["a"]))
print("Quantidade de e = " + str(vogais["e"]))
print("Quantidade de i = " + str(vogais["i"]))
print("Quantidade de o = " + str(vogais["o"]))
print("Quantidade de u = " + str(vogais["u"]))