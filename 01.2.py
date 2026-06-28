# Sistema de aprovação perante valores de saldo

saldo = 100
valor_a_levantar = float(input("Indique o valor a levantar: "))

saldo_restante = saldo - valor_a_levantar
if saldo >= valor_a_levantar:
    print(f"O valor restante é {saldo_restante}€")
else:
    print("Saldo negativo!")
    print("A Operação não foi concedida!")
    print(f"Para completar a operação, o Sr. precisa de {saldo_restante*-1}€")