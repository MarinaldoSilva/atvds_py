valor = int(input("Escolha um número"))
soma = 0

for i in range(1, valor + 1):
    if i % 2 == 0:
        soma += i
        print(f"{i} é par")
print(f"Soma dos pares: {soma}")