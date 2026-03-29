class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf


class Conta:
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
        self.historico = []

    def registrar(self, operacao):
        self.historico.append(operacao)