# Sistema de classificação por idade

# Criança (<13)
# Jovem (13–17)
# Adulto (18–64)
# Sénior (65+)

idade = int(input("Idade: "))
if idade <= 0:
    print("A tua idade humana é imposivel")
elif idade <= 13:
    print("Tu és uma Criança")
elif idade <= 17:
    print("Tu és um Jovem")
elif idade <= 64:
    print("Tu és um Adulto")
else:
    print("Tu és um Sénior")