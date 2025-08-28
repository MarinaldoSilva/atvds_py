class Pet():
    
    def __init__(self):
        self._nome = ""
        self._idade = ""
        self._peso = "peso"

    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return self._idade
    
    def get_peso(self):
        return self._peso

    global exception_definition
    exception_definition = ("valor vazio ou nulo")
    
    def set_nome(self, valor):
        if valor or valor == "":
            return exception_definition
        self.nome = valor

    def set_idade(self, valor):
        if int(valor) or int(valor) <= 0:
           return exception_definition
        self.idade = valor
        
    def set_peso(self, valor):
        if isinstance(valor, int) or isinstance(valor, int) <= 0:
            return exception_definition
        self.peso = valor
    
    def exibir_info(self):
        info = f"Nome: {self.get_nome()}, idade: {self.get_idade()}, peso: {self.get_peso()}"
        return info

def menu():
    print("----Cadastro de Pet-----")
    print("1 - Definir/Alterar nome do pet")
    print("2 - Definir/Alterar idade do pet")
    print("3 - DefDefinir/Alterar peso do pet")
    print("4 - exibir info do pet")
    print("sair")

    
    p = Pet()   

    while True:
        op = int(input("escolha uma opção: "))
        menu()
        match op:
            case 1:
                nome = input("nome do pet: ")
                p.set_nome(nome)
            case 2:
                idade = input("idade do pet: ")
                idade_int = int(idade)
                p.set_idade(idade_int)
            case 3:
                peso = input("peso do pet: ")
                peso_int = float(peso)
                p.set_peso(peso_int)
            case 4:
                p.exibir_info()
            case 5:
                print("saindo...")
                break
            case _:
                print("opção invalida")

if __name__ == "__main__":
    menu()

            