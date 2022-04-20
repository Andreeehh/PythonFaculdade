meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto"
         , "setembro", "outubro", "novembro", "dezembro"]
def mes(n):
    if(n < 1 or n > 12):
        return "Mês inválido, digite um mês entre 1 e 12"
    return meses[n-1]
print(mes(int(input("Digite o N do mês"))))