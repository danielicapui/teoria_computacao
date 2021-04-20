class Estado:
    def __init__(self,nome,tipo,ligacao):
        self.nome=nome
        self.tipo=tipo
        self.ligacao=ligacao
    def getNome(self):
        return self.nome
    def getTipo(self):
        return self.tipo
    def getLigacao(self):
        return self.ligacao
    def moverEstado(self,simbolo,pilha_topo):
        #percorre as ligações
        for indice in self.getLigacao():
            #busca ligações em que o simbolo da cadeia é igual a variavel simbolo e topo é igual a pilha_topo
            if indice[0]==simbolo and indice[1]==pilha_topo:
                return indice[2],indice[3]
        return 666,666
class Pilha:
    def __init__(self,valorinicial):
        self.fila=valorinicial
    def getFila(self):
        return self.fila
    def adicionaFila(self,valor):
        for i in valor:
            self.getFila().append(i)
    def removerFila(self):
        self.getFila().pop()
    def isVazia(self):
        if len(self.getFila())==0 or self.getFila()[0] in ["l","lambda","666"]:
            print("Fila:",self.getFila())
            return True
        else:
            return False



class Teste:
    def __init__(self,estados,pilha,cadeia):
        self.estados=estados
        self.pilha=pilha
        self.cadeia=cadeia
        self.atual=estados[0]
    def getEstados(self):
        return self.estados
    def getPilha(self):
        return self.pilha
    def getCadeia(self):
        return self.cadeia
    def getEstado_Inicial(self):
        #pega o estado inicial
        for i in (self.getEstados()):
            if i.getTipo()[0]==1:
                self.atual=i
                return i
    
    def getAtual(self,destino):
        #pega o estado atual
        for i in self.getEstados():
            if i.getNome()==destino:
                self.atual=i
                return True
        
                
        print("Cadeia não aceita")
        return False
    def trilha(self):
        c=0
        letra="nada"
        for simbolo in self.getCadeia():
            if self.getPilha().isVazia!=False:
                topo=self.getPilha().getFila()[-1]
            else:
                topo="l"
            print("Simbolo:",simbolo)
            print("Fila:",topo)
            print("Estado atual:",self.atual.getNome())
            dado=self.atual.moverEstado(simbolo,topo)
            print("Destino:{}\nProdução:{}".format(dado[0],dado[1]))
            print("\n")
            if dado[0]==666 and dado[1]==666:
                print("Cadeia não aceita")
                return False
            elif dado[1] in ["l","lambda","666"]:
                self.getPilha().removerFila()
            else:
                self.getPilha().adicionaFila(dado[1])
            self.getAtual(dado[0])
            c=c+1
            letra=simbolo
        if self.atual.getTipo()[1]==1 and c==len(self.getCadeia()) and letra==self.getCadeia()[-1] and self.getPilha().isVazia()==True:
            print("cadeia aceita")
            return True
        else:
            print("cadeia não aceita")
            return False
            
               
            
            
def criarAutonomo():
    #Preciso da quantidade de estados do autonomo, do nome,do tipo 
    quantidade=int(input("Digite a quantidade de estados:\n"))
    estados=[]
    tipos=[0,0]
    print("0==falso\n1==Verdade\n")
    for i in range(quantidade):
        
        nome=input("Digite o nome do estado:\n")
        tipos[0]=int(input("Este é um estado inicial:\n"))
        tipos[1]=int(input("Este é um estado final:\n"))
        numero=int(input("Defina quantas ligações {} tem:\n".format(nome)))
        ligacao=[]
        
        print("Ligações são da forma e são separadas pelo símbolo ',' [entrada,pilha_topo,destino,producao]")
       #Aqui nós escreveremos as ligações
        for t in range(numero):
            l=input("Digite a ligação de número l{}:\n".format(t)).split(",")
            ligacao.append(l)
        #Essas duas últimas linhas é para criar o Estado com os dados digitados e armazenar
        state=Estado(nome,tipos,ligacao)
        estados.append(state)

    return estados



def criarPilha():
    #Precisa de um valor inicial
    valor=[]
    t=input("Digite o símbolo inicial:\n")
    for letra in t:
        valor.append(t)
    p=Pilha(valor)
    return p

def criarCadeia():
    #Criar uma cadeia para ser lida
    palavra=input("Digite a cadeia que vai ser testada:\n")
    cadeia=[]
    for letra in palavra:
        cadeia.append(letra)
    return cadeia
def interface():
    #laço principal e variaveis  principais com letra em maisculas
    is_game_over=False
    ESTADOS=[]
    CADEIA=[]
    PILHA=[]
    while(not is_game_over):
        op=int(input("Digite 0 para criar um autonomo;\nDigite 1 para criar a pilha;\nDigite 2 para criar a cadeia de entrada;\nDigite 3 para testar a cadeia;\nDigite 666 para sair do programa:\n"))
        if op==0:
            ESTADOS=criarAutonomo()
        elif op==1:
            PILHA=criarPilha()
        elif op==2:
            CADEIA=criarCadeia()
        elif op==3:
            print("\n")
            teste=Teste(ESTADOS,PILHA,CADEIA)
            teste.getEstado_Inicial()
            teste.trilha()
        elif op==666:
            is_game_over=True
        else:
            print("Opção não válida.")

def main():
    interface()
main()