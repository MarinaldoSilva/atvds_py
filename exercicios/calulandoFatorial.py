import math

numero = int(input("Escolha um número: "))

if numero <= 0:
    print("Número inválido")
else:
    fatorial = 1
    for i in range(1, numero +1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}")

print("Usando a biblioteca math")
#ou pode fazer assim

if numero <= 0:
    print("Número inválido")
else:
    fatorial = math.factorial(numero)
    print(f"O fatorial de {numero} é {fatorial}")