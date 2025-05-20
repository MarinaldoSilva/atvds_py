while True:
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    mensagem = input("Escolha a operação: ")
    if mensagem == "1":
        nume1 = float(input("Digite o primeiro número: "))
        nume2 = float(input("Digite o segundo número: "))
        res = nume1 + nume2
        print(f"A soma é {res}")
    elif mensagem == "2":
        nume1 = float(input("Digite o primeiro número: "))
        nume2 = float(input("Digite o segundo número: "))
        res = nume1 - nume2
        print(f"A subtração é {res}")
    elif mensagem == "3":
        nume1 = float(input("Digite o primeiro número: "))
        nume2 = float(input("Digite o segundo número: "))
        res = nume1 * nume2
        print(f"A multiplicação é {res}")
    elif mensagem == "4":
        nume1 = float(input("Digite o primeiro número: "))
        nume2 = float(input("Digite o segundo número: "))

        if nume2 != 0 and nume1 != 0:
            res = nume1 / nume2
            print(f"A divisão é {res}")
        else:
            print("Não é possível dividir por zero!")
    elif mensagem == "5":
        print("Saindo...")
        break