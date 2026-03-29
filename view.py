class View:
    def menu(self):
        print("\n1 - Criar Conta")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver Histórico")
        return input("Escolha: ")

    def ler_dados_cliente(self):
        nome = input("Nome: ")
        cpf = input("CPF: ")
        saldo = float(input("Saldo inicial: "))
        return nome, cpf, saldo

    def ler_valor(self):
        return float(input("Valor: "))

    def mostrar_historico(self, conta):
        print("\n--- Histórico ---")
        for h in conta.historico:
            print(h)