import SOAPpy

server = SOAPpy.SOAPProxy('http://localhost:8080/')
#entra com o usuario
def entraUsuario():
    print("insira login e senha")
    login = raw_input('login:')
    senha = raw_input('senha:')
    res = server.loginUsuario(login,senha)
    if (res == 0):
        print("error ao fazer login")
        return 0
    else:
        return res
    
#cadrastra novo usuario 
def novoUsuario():
    print("insira login e senha")
    login = raw_input('login:')
    senha = raw_input('senha:')
    res = server.novoUsuario(login,senha)
    print(res);

#define o destinarario da mensagem e chama mensagem
def memUsuario(idr):
    print("destinatarios disponiveis")
    res =server.selUsuario()
    for x in res:
        print(x[1])

    print("insira nome do destinatario")
    login = raw_input('nome:')
    res1=server.desUsuario(login)
    print ("memUsuario",res1[0][0])
    res=mensagem(idr,res1[0][0])
    return res

#fica enviando a mensagem e recebendo a atualizacao do banco
def mensagem(idr, idd):
    l=True
    while(l):
        men = raw_input('mensagem:')
        if (men == "sair"):
            l = False
        else:
            res1=server.mensagem(idr, idd, men)
        if (res1 == 1):
            print("mensagem enviada com susesso")

            res2 = server.recMensagem(idr, idd)
            for x in res2:
                print(str(x[1])+": "+str(x[0]))
        else:
            print("mensagem enviada nao cadstrado")

    return 0

def main():
    l = True
    while (l):
        resl = entraUsuario()
        if (len(resl) == 1):
            l = False
    l = True
    while (l):

        res = memUsuario(resl[0][0])
        if (res == 0):
            l = False

if __name__ == "__main__":
    main()


