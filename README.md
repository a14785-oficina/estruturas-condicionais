# TP04 — Estruturas Condicionais

**Disciplina:** Programação e Sistemas de Informação (PSI) — Módulo 3
**Trabalho Prático:** 04
**Turma:** 1.º I — N.º 14785
**Ano Letivo:** 2025/2026

Introdução às estruturas `if / elif / else` em quatro cenários progressivamente mais complexos: multibanco, classificação etária, maior de três números e sistema de desconto.

---

## Ficheiros

| Ficheiro | Enunciado |
|---|---|
| `01.1.py` | Multibanco — saldo e levantamento dinâmicos |
| `01.2.py` | Multibanco — saldo fixo de 100 euros com detalhe do valor em falta |
| `02.py` | Classificação etária: Criança / Jovem / Adulto / Sénior |
| `03.py` | Maior de 3 números sem usar `max()` |
| `04.py` | Sistema de desconto automático e personalizado |

---

## Exercícios

### 01.1.py — Multibanco (Valores Dinâmicos)

Enunciado: Pedir saldo e valor a levantar; autorizar ou rejeitar.

```python
saldo = float(input("Indique o valor do saldo: "))
valor_a_levantar = float(input("Indique o valor a levantar: "))
if saldo >= valor_a_levantar:
    print("Saldo positivo, aprovado!")
else:
    print("Saldo negativo, reprovado!")
```

---

### 01.2.py — Multibanco (Saldo Fixo com Detalhe)

Enunciado: Saldo fixo de 100 euros — mostrar exatamente quanto falta se insuficiente.

```python
saldo = 100
valor_a_levantar = float(input("Indique o valor a levantar: "))
saldo_restante = saldo - valor_a_levantar
if saldo >= valor_a_levantar:
    print(f"O valor restante e {saldo_restante}euros")
else:
    print("Saldo negativo!")
    print("A Operacao nao foi concedida!")
    print(f"Para completar a operacao, o Sr. precisa de {saldo_restante*-1}euros")
```

Nota: `saldo_restante * -1` converte o valor negativo em positivo para mostrar o montante em falta.

---

### 02.py — Classificação Etária

Enunciado: Pedir a idade e classificar em quatro faixas.

```python
idade = int(input("Idade: "))
if idade <= 0:
    print("A tua idade humana e impossivel")
elif idade <= 13:
    print("Tu es uma Crianca")
elif idade <= 17:
    print("Tu es um Jovem")
elif idade <= 64:
    print("Tu es um Adulto")
else:
    print("Tu es um Senior")
```

| Faixa | Categoria |
|---|---|
| <= 0 | Inválida |
| 1 a 13 | Criança |
| 14 a 17 | Jovem |
| 18 a 64 | Adulto |
| 65 ou mais | Sénior |

---

### 03.py — Maior de 3 Números

Enunciado: Pedir 3 números e mostrar o maior, sem usar `max()`.

```python
num1 = int(input("1.o Numero: "))
num2 = int(input("2.o Numero: "))
num3 = int(input("3.o Numero: "))
print("---")
if num1 > num2 and num1 > num3:
    print(f"O maior numero e {num1}")
elif num2 > num1 and num2 > num3:
    print(f"O maior numero e {num2}")
elif num3 > num2 and num3 > num1:
    print(f"O maior numero e {num3}")
else:
    print("Nao insire valores repetidos")
    print("Insire valores corretos")
```

Nota: o ramo `else` captura o caso em que dois ou mais valores são iguais.

---

### 04.py — Sistema de Desconto

Enunciado: Pedir o valor de compra e aplicar desconto automático ou personalizado.

```python
compra = float(input("Valor da compra: "))
desconto_input = float(input("Valor de aplicacao de desconto (em %, digite 0 para desconto automatico): "))
print("---")
valor_desconto = 0

if desconto_input == 0:
    if compra >= 100:
        valor_desconto = compra * 0.10   # 10% de desconto
    elif compra >= 50:
        valor_desconto = compra * 0.05   # 5% de desconto
    else:
        valor_desconto = 0               # Sem desconto
else:
    valor_desconto = compra * (desconto_input / 100)

compra_total = compra - valor_desconto
if valor_desconto > 0:
    print(f"O valor da compra com desconto de {valor_desconto:.2f}euros e de: {compra_total:.2f}euros")
else:
    print(f"O valor da compra sem desconto e de: {compra_total:.2f}euros")
```

| Valor da compra | Desconto automático |
|---|---|
| >= 100 euros | 10% |
| >= 50 euros | 5% |
| < 50 euros | 0% |
| Personalizado | Percentagem definida pelo utilizador |

---

## Conceitos Abordados

| Conceito | Descrição |
|---|---|
| `if / else` | Bifurcação entre dois caminhos |
| `if / elif / else` | Múltiplas condições exclusivas |
| `if` aninhado | Condicionais dentro de condicionais |
| `and` | Duas condições verdadeiras em simultâneo |
| `float()` | Suporta valores monetários decimais |
| f-string `:.2f` | Formatação para 2 casas decimais |

---

## Como Executar

```bash
git clone https://github.com/a14785-oficina/estruturas-condicionais.git
cd estruturas-condicionais
python3 01.1.py
```

---

## Navegação — Módulo 3

| Posição | Repositório |
|---|---|
| Anterior | [TP03 — Operadores](https://github.com/a14785-oficina/operadores) |
| Seguinte | [EXPA01 — Exercícios de Estruturas Condicionais](https://github.com/a14785-oficina/exercicios-estruturas-condicionais) |
| Portfólio | [oficina-jpc](https://github.com/a14785-oficina/oficina-jpc) |

---

*PSI — Módulo 3 — Programação Estruturada — OFICINA — 2025/2026*
