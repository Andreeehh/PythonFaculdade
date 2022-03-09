true = 1
while(true == 1):
    type = int(input("Digite o tipo da operação"
                     "\n1: somar"
                     "\n2: subtrair"
                     "\n3: multiplicar"
                     "\n4: dividir"
                     "\nOutros valores: sair do programa\n"))
    if type < 1 or type > 4:
        true = 0
        print("Até a próxima")
    else:
        n1 = float(input("Digite o primeiro numero\n"))
        n2 = float(input("Digite o segundo numero\n"))
        if type == 1:
            result = n1 + n2
            print("Resultado = " + str(result))
        elif type == 2:
            result = n1 - n2
            print("Resultado = " + str(result))
        elif type == 3:
            result = n1 * n2
            print("Resultado = " + str(result))
        elif type == 4:
            result = n1 / n2
            print("Resultado = " + str(result))
