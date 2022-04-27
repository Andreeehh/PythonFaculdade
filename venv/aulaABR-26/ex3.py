meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro"
         , "novembro", "dezembro"]
data = input("Digite uma data no modo dd/mm/aaaa")
data = data.split("/")
data[1] = meses[int(data[1]) - 1 ]
print(data[0] + " de " + data[1] + " de " +data[2])