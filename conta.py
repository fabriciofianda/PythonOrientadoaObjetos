class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objetos... {}".format(self))
        print("Construindo objetos... {}".format(Conta))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("Saldo equivalente a {} do Titular {} ".format(self.saldo, self.titular))

    def depositar(self, valor):
        self.saldo += valor

    def retirar(self, valor):
        self.saldo -= valor
