# Sistema de aprovação perante valores de saldo

saldo = float(input("Indique o valor do saldo: "))
valor_a_levantar = float(input("Indique o valor a levantar: "))
if saldo >= valor_a_levantar:
    print("Saldo positivo, aprovado!")
else:
    print("Saldo negativo, reprovado!")