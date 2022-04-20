def bissexto(ano):
    if (ano%4 == 0):
        return "Bissexto"
    else:
        return "Não bissexto"
print(bissexto(int(input("Digite um ano"))))