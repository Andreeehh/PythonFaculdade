n = int(input("Digite uma opção a ser realizada:"
                  "\nSair: 0"
                  "\nSoma: 1"
                  "\nSubtração: 2"
                  "\nProduto: 3"
                  "\nDivisão: 4"))
while n != 0:
    n1 = int(input("Digite o primeiro valor"))
    n2 = int(input("Digite o segundo valor"))
    if n == 1:
        print("Soma = " +str(n1+n2))
    elif n == 2:
        print("Subtração = " + str(n1 - n2))
    elif n == 3:
        print("Produto = " + str(n1 * n2))
    elif n == 4:
        print("Divisão = " + str(n1 / n2))
    n = int(input("Digite uma opção a ser realizada:"
                      "\nSair: 0"
                      "\nSoma: 1"
                      "\nSubtração: 2"
                      "\nProduto: 3"
                      "\nDivisão: 4"))