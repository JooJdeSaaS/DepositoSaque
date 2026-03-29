from model import Cliente, Conta
from service import ContaService
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.service = ContaService()
        self.conta = None

    def executar(self):
        while True:
            opcao = self.view.menu()

            if opcao == "1":
                nome, cpf, saldo = self.view.ler_dados_cliente()
                cliente = Cliente(nome, cpf)
                self.conta = Conta(cliente, saldo)

            elif opcao == "2":
                valor = self.view.ler_valor()
                self.service.depositar(self.conta, valor)

            elif opcao == "3":
                valor = self.view.ler_valor()
                self.service.sacar(self.conta, valor)

            elif opcao == "4":
                self.view.mostrar_historico(self.conta)

            else:
                print("Opção inválida")