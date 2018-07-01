"""
    SIMULADOR DE CAIXA ATM 
    ----------------------
    
    Tipos de moeda (US$, BitCoin)
    
    Operações:
        1) Retirada
        2) Consultas: Saldo, Extratos, Operações futuras, Comprovantes
        3) Transferências: Wire (Banco a Banco - TED) e DOC 
        4) Pagamento de Contas: Com boleto, Com numero CPF (bases de dados de contas possíveis)
        5) Compra de BitCoin
        6) Venda de BitCoin
        7) Recarga de Cartão de Débito (Black Card)
        8) Troca de senha
"""


import sqlite3 
import getpass

idCliente   = 0
idBanco     = 0
idAgencia   = 0
idConta     = 0
_saldoAtual = 0.00

clienteDados = ["nome",
                "senha",
                "banco",
                ["agencia0"],
                ["conta0"],
                ["tipoconta0"],
                "numcontas"
               ]

dbConn = sqlite3.connect("databasebankATM.db")


_dbCursor = dbConn.cursor()

_loggedOn = False


def checkDadosLoginClienteATM(banco, agencia, conta, senha) :
    checkLogin = dbLoginClienteATM(_dbCursor, banco, agencia, conta, senha)

    if (not checkLogin == True) :
        _loggedOn = False
        return False
    else :
        _loggedOn = True
        return True


def identificaCliente(idCliente) :
        dadosCliente                    = dbPegaDadosClientePorId(idCliente)
        clienteDados["nome"]            = dadosCliente["nome"]
        clienteDados["senha"]           = dadosCliente["senha"]
        clienteDados["banco"]           = dadosCliente["banco"]
        clienteDados["agencia0"]        = dadosCliente["agencia"][0]
        clienteDados["conta0"]          = dadosCliente["conta"][0]
        clienteDados["tipoconta0"]      = dadosCliente["tipoconta"][0]

        clienteDados["numcontas"]       = dadosCliente["numContas"]
        if (clienteDados["numcontas"] > 1) :
            while contaContas in range (1,numcontasCliente) :
                contasCliente["agencia"][contaContas] = dadosCliente["agencia"][contaContas]
                contasCliente["conta"][contaContas] = dadosCliente["conta"][contaContas]
                contasCliente["tipoconta"][contaContas] = dadosCliente["tipoconta"][contaContas]
                                

                    
                    
def dbLoginClienteATM(cursor) :
    
    banco = input("Informe o código do Banco: ")
    agencia = input("Informe a agência: ")
    conta = input("Informe a conta: ")
    senha = getpass.getpass(prompt="Informe a senha: ")
    
    _idConta = 0

    _sqlQuery = "SELECT `contas`.`id_conta` FROM `contas`, `clientes_contas`, `clientes`  WHERE `contas`.`banco` = '%s' AND `contas`.`agencia` = '%s' AND `contas`.`conta` = '%s' AND `clientes_contas`.`id_conta` = `contas`.`id_conta` AND `clientes`.`id_cliente` = `clientes_contas`.`id_cliente` AND `clientes`.`senha` = '%s'" % (banco, agencia, conta, senha)

    #print(_sqlQuery)

    if cursor.execute(_sqlQuery) :
        _idConta = cursor.fetchone()[0]
    
    return _idConta
        
        
tentativas = 0

_telaAnsi = "[?7h[40m[2J[0;1;44mÉÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ»[2;1Hº                                                                              º[3;1Hº                                                                              º[4;1Hº                                                                              º[5;1Hº                                                                              º[6;1Hº                     ÜÛÛÛÛÛÛÛÜ  ÜÛÛÛÛÛÛÛÛÛÛÜ ÜÛÛÜ   ÜÛÛÜ                      º[7;1Hº                    ÛÛÛÛßßßÛÛÛÛ ßßßßÛÛÛÛßßßß ÛÛÛÛÛÜÛÛÛÛÛ                      º[8;1Hº                    ÛÛÛÛÜÜÜÛÛÛÛ     ÛÛÛÛ     ÛÛÛÛÛÛÛÛÛÛÛ                      º[9;1Hº                    ÛÛÛÛÛÛÛÛÛÛÛ     ÛÛÛÛ     ÛÛÛÛ ß ÛÛÛÛ                      º[10;1Hº                    ÛÛÛÛ   ÛÛÛÛ     ÛÛÛÛ     ÛÛÛÛ   ÛÛÛÛ                      º[11;1Hº                    ßÛÛß   ßÛÛß     ßÛÛß     ßÛÛß   ßÛÛß                      º[12;1Hº                                                                              º[13;1Hº               BEM-VINDO AO SEU CAIXA ELETRONICO PARA BITCOINS                º[14;1Hº                                                                              º[15;1Hº                                                                              º[16;1Hº                       Informe seu Banco: [        ]                          º[17;1Hº                     Informe sua Agencia: [        ]                          º[18;1Hº                         Informe a Conta: [        ]                          º[19;1Hº                         Informe a Senha: [        ]                          º[20;1Hº                                                                              º[21;1Hº                                                                              º[22;1Hº                                                                              º[23;1HÈÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍÍ¼[24;1H                                                                                [25;1H                                                                               [40m
[A[79C[44m [0m[255D"
                    
print (_telaAnsi)

while tentativas < 3 :
    id_conta = dbLoginClienteATM(_dbCursor)
    if (id_conta == None) :
        tentativas += 1
        if tentativas < 3 :
            print("Combinação Agência/Conta/Senha Inválida! Restam %i tentativas antes da conta ser bloqueada." % int(3 - tentativas))
        else :
            print ("Conta bloqueada por excesso de tentativas! Procure sua agência/gerente para regularizar. Obrigado.")
    else :
        print("Id Conta: %s" % str(id_conta))
        print("Acesso Liberado! Aguardo Sistema em carregamento!")
        break


    
"""

amount=input ("Qual o valor da sua retirada?")
amount=int(amount)
ot=amount//1000
fh=(amount-(ot * 1000))// 500
th=(amount-(ot *1000)-(fh*500))//200
oh=(amount-(ot *1000)-(fh*500) - (th*200))//100
f=(amount-(ot *1000)-(fh*500) - (th*200) - (oh*100))//50
t=(amount-(ot *1000)-(fh*500) - (th*200) - (oh*100) -(f*50))//20

print("Você receberá:")

if ot>1 or ot==0 :
    print ("%i notas de 1,000"%(ot))
else :
    print ("%i nota de 1,000"%(ot))
if fh>1 or fh==0 :
    print ("%i notas de 500"%(fh))
else :
    print ("%i nota de 500"%(fh))
if th>1 or th==0 :
    print ("%i notas de 200"%(th))
else :
    print ("%i nota de 200"%(th))
if oh>1 or oh==0 :
    print ("%i notas de 100"%(oh))
else :
    print ("%i nota de 100"%(oh))
if f>1 or f==0 :
    print ("%i notas de 50"%(f))
else :
    print ("%i nota de 50"%(f))
if t>1 or t==0 :
    print ("%i notas de 20"%(t))
else :
    print ("%i nota de 20"%(t))

print("Sua transação foi concluída com sucesso! Tenha um excelente dia.")

"""