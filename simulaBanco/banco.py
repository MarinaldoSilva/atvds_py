saldo = 1000

while True:
    print("Selecione uma opção:")
    print("1. Saldo")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Sair")

    opcao =  input("Escolha uma opção: ")

    if opcao == "1":
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao == "2":
        valor = float(input("Digite o valor a depositar:"))
        if valor > 0:
            saldo+=valor
            print(f"deposito feito com sucesso!")
    if opcao == "3":
        valor = float(input("Digite o valor a sacar:"))
        if valor <= saldo:
            saldo-=valor
            print(f"Saque feito com sucesso!")
        else:
            print(f"Saldo insuficiente!")
    elif opcao == "4":
        print("Saindo...")
        break
