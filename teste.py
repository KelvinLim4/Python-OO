
def cria_conta(numero, titular, saldo, limite):
    conta = {"nume": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

#Função para depositar dinheiro
def deposita(conta, valor):
    conta ["saldo"] += valor

#Função para sacar dinheiro
def saca(conta, valor):
    conta ["saldo"] -= valor

def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))