m1 = ["andre", "ricardo", "flavio", "lucia", "ana", "renata"]
m2 = ["andre", "anderson", "marta", "lucia", "laura", "renata"]
c1 = set(m1)
c2 = set(m2)
print("Quantidade de alunos matriculados nas duas materias: " + str(len(c1.intersection(c2))))