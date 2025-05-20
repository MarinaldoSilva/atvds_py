import math

quadrados_impares = [pow(x,2) for x in range(1,11) if x % 2 !=0]
print(quadrados_impares)

print("outro exemplo com for avançado")

texto = "Olá, Mundo"

consoantes = [letra for letra in texto if letra.lower() not in 'aeiou']
#loop executa primeiro, atribuindo letra a cada caractere de texto. ✅ Depois, verifica se letra está fora da lista de vogais (not in 'aeiou'). ✅ Se a condição for verdadeira, a variável letra é adicionada à lista.
print(consoantes)
print("outro exemplo agora de forma tradicional")

consoantes2 = []

for letra in texto:
    if letra.lower() not in 'aeiou':
        consoantes2.append(letra)
print(consoantes2)