# Sistema de Desconto

# Criar programa que:
# Peça valor da compra
# Aplicar desconto:
# >= 100 → 10%
# >= 50 → 5%
# < 50 → sem desconto

compra = float(input("Valor da compra: "))
desconto_input = float(input("Valor de aplicação de desconto perante a compra (em %, digite 0 para desconto automático): "))

print("---")

valor_desconto = 0

if desconto_input == 0:
    if compra >= 100:
        valor_desconto = compra * 0.10  # 10% de desconto
    elif compra >= 50:
        valor_desconto = compra * 0.05  # 5% de desconto
    else:
        valor_desconto = 0  # Sem desconto
else:
    # Aplicar desconto personalizado pelo usuário
    valor_desconto = compra * (desconto_input / 100)

compra_total = compra - valor_desconto

if valor_desconto > 0:
    print(f"O valor da compra com desconto de {valor_desconto:.2f}€ é de: {compra_total:.2f}€")
else:
    print(f"O valor da compra sem desconto é de: {compra_total:.2f}€")