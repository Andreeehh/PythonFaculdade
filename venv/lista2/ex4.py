data = input ("Digite a data de nascimento dd/mm/yyyy")
arr = data.split("/")
d = int(arr[0])
m = int(arr[1])
a = arr[2]
if (m==12 and d >=22) or (m ==1 and d <=22):
    print ("Capricornio")
elif (m == 1 and d >=21) or (m == 2 and d <= 18) :
    print ("Aquário")
elif (m == 2 and d >=19) or (m ==3 and d <= 22):
    print("Peixes")
elif (m == 3 and d >=21) or (m ==4 and d <=22):
    print ("Aries")
elif (m == 4 and d >=21) or (m ==5 and d <=22):
    print ("Touro")
elif (m == 5 and d >=21) or (m == 6 and d <= 22) :
    print ("Gêmeos")
elif (m == 6 and d >=21) or (m ==7 and d <=22):
    print("Câncer")
elif (m == 7 and d >=23) or (m ==8 and d <=22):
    print ("Leão")
elif (m == 8 and d >=23) or (m == 9 and d <=22):
    print("Virgem")
elif (m == 9 and d >= 23) or (m == 10 and d <=22):
    print("Libra")
elif (m == 10 and d >=23) or (m ==11 and d <=21):
    print ("Escorpião")
elif (m == 11 and d >=22) or (m ==12 and d <= 21):
    print ("Sargitário")