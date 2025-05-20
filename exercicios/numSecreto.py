numSecreto = 7
numSecreto2 = 10
tentativa = 5

adivinhou = False
adivinhou2 = False

while tentativa > 0 and (not adivinhou and not adivinhou2):
    print(f"Você tem {tentativa} tentativas")
    palpite1 = int(input("Digite um número entre 1 e 10: "))
    palpite2 = int(input("Digite um número entre 1 e 10: "))

    if palpite1 == numSecreto:
        print("Você acertou o primeiro número!")
        adivinhou = True
    else:   
        print("Você errou o primeiro número!")
        tentativa -= 1

    if palpite2 == numSecreto2:
        print("Você acertou o segundo número!")
        adivinhou2 = True 
    else:
        print("Você errou o segundo número!")
        tentativa -= 1
    


