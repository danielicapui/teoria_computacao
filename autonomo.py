class Estado:
    def __init__(self,inicial,final):
        self.inicial=inicial
        self.final=final

    def reacoes(self):
        print("As ligações são no formato estado_atual entrada estado_de_destino, exemplo (0,1,1) para lambda digite 666")
        r=int(input("Diga quantas ligações este estado possuí:"))
        self.inu=[]
        for i in range(r):
            print("Digite a ligação {} do estado:".format(i))
            e=input().split(",")
            self.inu.append(e)
    def mostrarReacoes(self):
        print(self.inu)
class Linguagem:
    def __init__(self,palavra):
        self.palavra=palavra

class Teste:
    def __init__(self,estados,ini,finais):
        self.estados=estados
        self.ini=ini
        self.finais=finais
    def Cadeia(self):
        cadeia=input("Digite a cadeia")
        self.entradas=[]
        for i in cadeia:
            self.entradas.append(i)
        return self.entradas
    def percorrer(self):
        self.atual=self.ini
        found=False
        for i in range(len(self.entradas)):
            print("Estado atual:q{} com leitura de {}".format(self.atual,self.entradas[i]))
            for q in range(len(self.estados)):  
                for c in range(len(self.estados)):
                    if (self.atual==self.estados[q].inu[c][0]) and (self.estados[q].inu[c][1]==self.entradas[i]):
                        self.atual=self.estados[q].inu[c][2]
                        found=True
                        break
            if found==False:
                print("Cadeia não aceita")
                break
            if i!=len(self.entradas)-1:
                found=False
            if i==len(self.entradas)-1:
                if self.verificar()==True:
                    break
            print("q{}".format(self.atual))
                 
            
    def verificar(self):
        for i in self.finais:
            if str(self.atual)==str(i):
                print("Cadeia aceita")
                print(self.entradas)
                return True
        print("Cadeia não aceita")
        return False
def adicionarLinguagem():
    print("As linguagens devem ser no formato minusculas. Exemplo de linguagem: a bn n>0 ")
    regra=input("Qual a regra?").split()
    for i in range(len(regra)):
        regra[i]==entrada


def criarAutonomo(estado_inicial):
    n=int(input("Quantos estados tem nesse AFD?:\n"))
    estado=[]
    ei=9
    estados_finais=[]
    for i in range(n):
        es=int(input("Este é um estado final?;0 ou 1\n"))
        if es==1:
            estados_finais.append(i)
        if estado_inicial==False:
            ei=int(input("Este é um estado inicial?\n"))
            if ei==1:
                estado_inicial=str(i)
        else:
            ei=0
        shika=Estado(ei,es)
        shika.reacoes()
        estado.append(shika)
    return estado,estado_inicial,estados_finais


def Interface():
    print("Bem-vindo a interface. 0==false, 1==true")
    estados=0
    estado_inicial=False
    linguagem=False
    while(True):
        op=int(input("Digite 1 para digitar uma AFD;\nDigite 2 para digitar um AFND;\nDigite 666 para encerrar o programa;\nDigite 3 para adicionar uma linguagem;\nDigite 4 para testar o autônomo AFD;\nDigite 5 para testar o autônomo AFND;\nDigite 6 para mostrar o autônomo;\nDigite 7 para limpar os autônomos;\n"))
        if op==1:
            estados,estado_inicial,estados_finais=criarAutonomo(estado_inicial)
        elif op==2:
            pass
        elif op==666:
            break
        elif op==3:
            print("Em desenvolvimento.")
            #adicionarLinguagem()
        elif op==4:
            teste=Teste(estados,estado_inicial,estados_finais)
            teste.Cadeia()
            teste.percorrer()
            
def main():
    Interface()
main()