import SOAPpy
from conexao import insertUsuDB,selectUsuDB,insertMenDB,selectMenDB,selectloginDB,selectDesDB
import datetime

#faz login
def loginUsuario(login,senha):
        res=selectloginDB(login, senha)
        return res

#insere novo usuario
def novoUsuario(login,senha):
        res=insertUsuDB(login, senha)
        if(res==1):
                return "usuario cadstrado com susesso"
        else:
                return "error usuario nao cadstrado"
#tras usuarios disponiveis
def selUsuario():
        res=selectUsuDB()
        return res

#tras id destinatario disponiveis
def desUsuario(login):
        res=selectDesDB(login)
        return res

#salva mensagem no banco
def mensagem(idr,idd,men):
        data = datetime.datetime.now()
        res = insertMenDB(idr, idd, men, data)
        return res

#tras entre os usuarios
def recMensagem(idr,idd):
        res=selectMenDB(idr, idd)
        return res

#inicia o serve e registra a funcoes
server = SOAPpy.SOAPServer(("localhost", 8080))
server.registerFunction(novoUsuario)
server.registerFunction(loginUsuario)
server.registerFunction(mensagem)
server.registerFunction(recMensagem)
server.registerFunction(selUsuario)
server.registerFunction(desUsuario)
server.serve_forever()