# Sistema de enunciação do numero maior de 3 numeros

num1 = int(input("1.º Numero: "))
num2 = int(input("2.º Numero: "))
num3 = int(input("3.º Numero: "))

print("---")

if num1 > num2 and num1 > num3:
    print(f"O maior numero é {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior numero é {num2}")
elif num3 > num2 and num3 > num1:
    print(f"O maior numero é {num3}")
else:
    print("Não insire valores repetidos")
    print("Insire valores corretos")

# if num1 > num2 and num1 > num3:
#     print(f"O maior numero é {num1}")
# elif num2 > num3: #elif num2 > num1 and num2 > num3:
#     print(f"O maior numero é {num2}")
# else: #elif num3 > num2 and num3 > num1:
#     print(f"O maior numero é {num3}")