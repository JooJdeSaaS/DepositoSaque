class ContaService:
    def depositar(self, conta, valor):
        if valor > 0:
            conta.saldo += valor
            conta.registrar(f"Depósito: +R$ {valor:.2f}")
        else:
            print("Valor inválido para depósito")

    def sacar(self, conta, valor):
        if valor <= conta.saldo:
            conta.saldo -= valor
            conta.registrar(f"Saque: -R$ {valor:.2f}")
        else:
            print("Saldo insuficiente")