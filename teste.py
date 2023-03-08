def cria_conta(numero, titular, saldo, limite):
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo, "Limite": limite}
    return conta

def deposita(conta, valor):
    conta["Saldo"] += valor

def saque(conta, valor):
    conta["Saldo"] -= valor

def extrato(conta):
    print("Saldo equivale - {}".format(conta["saldo"]))