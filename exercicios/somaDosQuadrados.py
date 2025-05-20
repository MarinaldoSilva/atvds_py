valor = int(input("Escolha um número \n"))
soma = 0

for i in range(1, valor + 1):
    elevado = pow(i, 2)
    print(f"{i} elevado ao quadrado é {elevado}")
    soma += elevado
print(f"Soma dos quadrados: {soma}")