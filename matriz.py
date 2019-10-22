import numpy as np
import glob


np.set_printoptions(precision=3)


class matriz:

    """"
    Tarefa 1
    ========
    A partir de uma matriz 3x3 qualquer obter a forma triangularizadae depois criar
    um algorítimo de retrosubstituição que solucione o sistema a partir da matriz
    triangularizada.
    ========
    """""

    def eliminacao_gaussiana(self):
        for i in range(self.linhas):
            self.zerar_ge(i)
        return self.mtz

    def retrosubstituicao(self):
        Xi = self.mtz[self.n_linha, self.m_coluna] / self.mtz[self.n_linha, self.n_linha]
        respostas = [Xi]
        linha = []
        for i in range(self.n_linha - 1, -1, -1):

            linha = [self.mtz[i, j] for j in range(i + 1, self.m_coluna)]

            seq = self.mtz[i, self.m_coluna]
            for k in range(len(respostas)):
                seq -= (respostas[k] * linha[k])

            Xn = (1 / self.mtz[i, i]) * seq
            respostas = [Xn] + respostas
            linha = []
        return respostas

    """
    ========
    Tarefa 2: Criar um algorítmo que resolva o problema do valor de contorno para equação:
    y"(t)-y'(t)=25t em [0,1] onde y(0)=y(1)=0
    mtzproximando os valores em 5 subintervalos iguais, isto é, em 4 pontos interior da grade.
    ========
    """

    def valoresContorno(self):
        self.gauss_jordan()
        print("mtz matriz reduzida por Gauss Jordan é:\n\n", self.mtz, "\n")
        forma = self.forma()
        for i in range(0, forma[1] - 1):
            print("\ty(t%d) = %.2f" % (i + 1, self.mtz[i, (forma[1] - 1)]))

    '''
    Tarefa 3
    =========
    Criar um algorítmo que reduza uma matriz qualquer 3x5 a sua forma escalonada em linha e 
    encontre suas colunas bases.
    =========
      '''

    def escalonada_linha(self):
        pivos = []
        for i in range(self.m_coluna - 1):
            pivolinha, pivocoluna = self.pivo_el(i)
            if pivolinha != "zero":
                if (pivolinha, pivocoluna):
                    local = (pivolinha, pivocoluna)
                    pivos.append(local)
                    self.mtz = self.zerar_el(pivolinha, pivocoluna)
        count = 0
        for pivo in pivos:
            count += 1
            print("A coluna base %d" %count)
            self.imprime_coluna(pivo[1])

        print("\nA matriz escalonada em linha:\n", self.mtz, "{ Rank = %d } \n" % (len(pivos)))
        return self.mtz, pivos, len(pivos)

    '''
    Tarefa 4
    =========
    Escrever um algorítmo numa linguagem  de maior afinidade que você tenha que tome um sistema 5x5 
    homogêneo e decida se ele é consistente ou não consistente. Caso seja consistente decida se ele tem 
    uma única solução ou mais de uma solução e se tem infinitas soluções e encontre as soluções das 
    variáveis básicas em função das variáveis livres.
    =========
      '''
    def homogeneo(self):

        mtz, pivos, rank = self.reduzida_linha()
        colunas_basicas = [pivo[1] for pivo in pivos]
        colunas_livres = [x for x in range(self.colunas) if not x in colunas_basicas]
        # A primeira parte do código verifica as condições de consistência
        for i in range(self.linhas):
            quantzero = 0
            ultimo = self.mtz[i][self.m_coluna]
            for j in range(self.colunas - 1):
                if self.mtz[i][j] is 0:
                    quantzero += 1
                # Uma matriz não é consistênte se aparece uma linha ( 0 0 · · · 0 | α ), α != 0
                if (quantzero == (self.m_coluna - 1)) and ultimo != 0.0: return "INCONSISTENTE"

            if self.m_coluna in colunas_basicas : return "INCONSISTENTE"

        #A segunda parte do código: Se a matriz é consitente

        # verifica se a matriz tem uma única solução
        if rank == self.linhas:
            print("A matriz tem somente a solução trivial.")
            return None

        # A seguir escreve-se a variáveis básicas em função das livres
        dois = self.dois_naozero()
        l1 = dois[0][0]
        c1 = dois[0][1]
        l2 = dois[1][0]
        c2 = dois[1][1]
        #pego a coluna dos dois não nulos
        lista = [0 for i in range(self.colunas-1)]

        if c1 in colunas_basicas:
            lista[c1] = "x"+ str(c1+1) + "= " + str(-(self.mtz[l1,c1])/self.mtz[l2,c2])+"x"+ str(c2+1)
            lista[c2] = "x" + str(c2+1) + " é livre"
        else:
            lista[c2] = str(-(self.mtz[l2,c2])/self.mtz[l1,c1])
            lista[c1] = "x" + str(c2+1) + " é livre"

        for i in range(self.linhas):
            if i in colunas_livres and lista[i] == 0 :
                lista[i] = "x"+ str(i+1) + " é livre"

            if i in colunas_basicas and lista[i] == 0:
                s  = "x" + str(i+1) + "= "
                lista[i] = s
                for j in range(self.linhas):
                    if i == j: pass
                    elif self.mtz[i,j] != 0:
                        lista[i] += ["-", "+"][-(self.mtz[i,j]) > 0] + str(self.mtz[i,j])+"x"+str(j+1)+ " "
            if lista[i] == s:
                for k in range(self.linhas):
                    if self.mtz[k,i] != 0:
                        lista[i] += ["-", "+"][-(self.mtz[k,i]) > 0] + str(self.mtz[k,i])+"x"+str(k+1)+ " "
        for item in lista:
            print("\n" + str(item) )

        return self.mtz
    '''
    Tarefa 5
    =========
    Escrever um algorítmo numa linguagem  de maior afinidade que você tenha que tome um sistema 5x5 
    homogêneo e decida se ele é consistente ou não consistente. Caso seja consistente decida se ele tem 
    uma única solução ou mais de uma solução e se tem infinitas soluções e encontre as soluções das 
    variáveis básicas em função das variáveis livres.
    =========
      '''
    def multiplica (self, B):

        if self.linhas != B.colunas : return "Não é conformável no produto AB"

        C = np.zeros((self.linhas,B.colunas), dtype= np.float)

        for i in range(self.linhas):
           for j in range(B.colunas):
               for k in range(B.linhas):
                   C[i][j] += self.mtz[i][k] * B.mtz[k][j]
        return C

    def inv_gj(self):
        identidade = self.identidade
        for linha in range(self.linhas):
            linhamaior = self.maior_coluna(linha)
            if linhamaior != linha:
                for i in range(self.colunas):
                    aux = self.mtz[linhamaior, i]
                    self.mtz[linhamaior, i] = self.mtz[linha, i]
                    self.mtz[linha, i] = aux
                    aux2 = identidade[linhamaior, i]
                    identidade[linhamaior, i] = identidade[linha, i]
                    identidade[linha, i] = aux2
            pivo = self.mtz[linha, linha]
            for h in range(0, self.colunas):
                self.mtz[linha, h] /= pivo
                identidade[linha,h]/= pivo
            for i in range(0, self.linhas):
                if i == linha:
                    pass
                elif self.mtz[i, linha] == 0:
                    pass
                else:
                    x = self.mtz[i, linha] / self.mtz[linha, linha]
                    for j in range(0, self.colunas):
                        self.mtz[i, j] -= x * self.mtz[linha, j]
                        identidade[i, j] -= x * identidade[linha, j]
        return self.mtz, identidade

    def __init__(self, matrizmtz):
        self.mtz = matrizmtz
        self.colunas = self.colunas()
        self.linhas = len(self.mtz)
        self.n_linha = self.linhas - 1
        self.m_coluna = self.colunas - 1
        self.original = self.copia()
        self.identidade = self.identidade()

    # zerar_ge : Executa operações da eliminação gaussiana
    def zerar_ge(self, coluna):
        if self.linhas != self.colunas - 1:
            raise ValueError("O número de linhas e colunas não é compativél!")
        self.pivo_ge(coluna)
        #começa coluna+1 pra começar a zerar o abaixo do pivo
        for i in range(coluna + 1, self.linhas):
            if self.mtz[i, coluna] == 0:
                pass
            else:
                x = self.mtz[coluna, coluna] / self.mtz[i, coluna]

                for j in range(coluna, self.colunas):
                    self.mtz[i, j] = x * self.mtz[i, j] - self.mtz[coluna, j]

        return self.mtz

    # pivo_ge : posiona o maior elemento de uma coluna para ser o pivo
    def pivo_ge(self, colun):
        linha = self.maior_coluna(colun)
        if linha != colun:
            self.troca_linha(linha, colun)
            return self.mtz
        else:
            return self.mtz

    #gauss_jordan: faz eliminação de gauss jordan
    def gauss_jordan(self):
        for i in range(self.linhas):
            self.zerar_gj(i)
        return self.mtz

    #zerar_gj: executa operações para zerar colunas a partir do pivo
    def zerar_gj(self, linha):
        self.pivo_ge(linha)
        pivo = self.mtz[linha, linha]
        for h in range(0, self.colunas):
            self.mtz[linha, h] /= pivo
        for i in range(0, self.linhas):
            if i == linha:
                pass
            elif self.mtz[i, linha] == 0:
                pass
            else:
                x = self.mtz[i, linha] / self.mtz[linha, linha]
                for j in range(0, self.colunas):
                    self.mtz[i, j] -= x * self.mtz[linha, j]
        return self.mtz

    #reduzida_linha : executa as operações da forma reduzida escalonada em linha
    def reduzida_linha(self):
        pivos = []
        for i in range(self.m_coluna - 1):
            pivolinha, pivocoluna = self.pivo_el(i)
            if pivolinha != "zero" :
                local = (pivolinha, pivocoluna)
                pivos.append(local)
                self.mtz = self.zerar_rel(pivolinha, pivocoluna)
                for i in pivos:
                    c = self.mtz[i[0], i[1]]
                for j in range(self.colunas):
                    self.mtz[i[0], j] /= c
        return self.mtz, pivos, len(pivos)

    # zerar_el : executa operações para zerar as colunas na forma reduzida escalonada em linha
    def zerar_rel(self, linhaPivo, colunaPivo):
        c = self.mtz[linhaPivo, colunaPivo]
        for m in range(self.colunas):
            self.mtz[linhaPivo, m] /= c
        for i in range(0, self.linhas):
            if i == linhaPivo:
                pass
            elif self.mtz[i][colunaPivo] == 0:
                pass
            else:
                x = self.mtz[i][colunaPivo] / self.mtz[linhaPivo][colunaPivo]
                for j in range(colunaPivo, self.colunas):
                    self.mtz[i][j] -= x * self.mtz[linhaPivo][j]
        return self.mtz

    #zerar_el : Executa operações para a forma escalonada em linha
    def zerar_el(self, linhaPivo, colunaPivo):
        for i in range(linhaPivo + 1, self.linhas):
            if self.mtz[i][colunaPivo] == 0:
                pass
            else:
                x = self.mtz[i][colunaPivo] / self.mtz[linhaPivo][colunaPivo]
                for j in range(colunaPivo, self.colunas):
                    self.mtz[i][j] -= x * self.mtz[linhaPivo][j]
        return self.mtz

    # pivo_el : encontra a primeira entrada não nula e posiciona
    def pivo_el(self, linha):
         for coluna in range(linha, self.colunas):
            if self.mtz[linha,coluna] != 0:
                return linha, coluna
            else:
                for j in range(linha + 1, self.linhas):
                    if self.mtz[j,coluna] != 0:
                        self.troca_linha(linha, j)
                        return linha , coluna
         return "zero", "zero"

    def dois_naozero(self):
        for linha in range(self.linhas):
            lista = []
            naonulo = 0
            for coluna in range(self.colunas):
                if self.mtz[linha][coluna] != 0:
                    lista.append((linha, coluna))
                    naonulo += 1
            if naonulo == 2:
                return lista
        return False

    def imprime_coluna(self, coluna):
        for i in range(self.linhas):
            print("| ", self.mtz[i][coluna], " |")

    def imprime_linha(self, linha):
        print("-->", end=" ")
        for i in range(self.colunas):
            print(self.mtz[linha][i])

    def identidade(self):
        linhas, colunas = self.forma()
        identidade = np.zeros((linhas, colunas), dtype=np.float)
        if linhas == 1 or colunas == 1:
            identidade[0,0] = 1
            return identidade
        for i in range(linhas):
            identidade[i, i] = 1
        return identidade

    def lista_linha(self, linha):
        lista = []
        for i in range(self.colunas):
            x = self.mtz[linha][i]
            lista.append(x)
        return lista

    def troca_linha(self, linha1, linha2):
        for i in range(self.colunas):
            aux = self.mtz[linha1, i]
            self.mtz[linha1, i] = self.mtz[linha2, i]
            self.mtz[linha2, i] = aux

    def maior_coluna(self, coluna):
        maior = -999999999
        linhaMaior = coluna
        for i in range(coluna, self.linhas):
            if self.mtz[i, coluna] > maior and self.mtz[i, coluna] != 0:
                maior = self.mtz[i, coluna]
                linhaMaior = i
        return linhaMaior

    def bubblesort(self):
        nulos = 0
        lista = []
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.mtz[i,j] == 0:
                    nulos +=1
            lista.append(nulos)
            nulos =0
        while True:
            trocado = False
            for i in range(len(lista)-1):
                if lista[i] > lista[i+1]:
                    aux = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = aux
                    self.troca_linha(i,i+1)
                    trocado = True
            if not trocado: break
        return self.mtz

    def origem(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                self.mtz[i, j] = self.original[i, j]

    def copia(self):
        linhas, colunas = self.forma()
        copia = np.zeros((linhas, colunas), dtype=np.float)
        for i in range(linhas):
            for j in range(colunas):
                copia[i, j] = self.mtz[i, j]
        return copia

    def colunas(self):
        coluna = 0
        print(self.mtz)
        for i in self.mtz[0]:
            coluna += 1
        return coluna

    def forma(self):
        return (self.linhas, self.colunas)

    def __str__(self):
        return str(np.asmatrix(self.mtz))


def txt_matriz():
    i = 1
    arquivos = []
    print("\nOs arquivos .txt no diretório são:\n")
    for file in glob.glob("atividades/*.txt"):
        print("mtzrquivo %d : %s" % (i, file))
        i += 1
        arquivos.append(file)
    num = int(input("Digite onde está a matriz:"))
    with open(arquivos[num - 1]) as f:
        linhas = f.readlines()
    l = []
    for i in linhas:
        if "\n" in i:
            l.append(i.replace("\n", ""))
        else:
            l.append(i)
    forma = l[0].split("x")
    linhas, colunas = int(forma[0]), int(forma[1])
    matriz = np.zeros((linhas, colunas), dtype=np.float)
    for i in range(1, linhas + 1):
        mtzl = l[i]
        mtz = mtzl.split(" ")
        for j in range(0, colunas):
            matriz[i - 1, j] = float(mtz[j])
    return matriz

def digitar_matriz():
    formas = input("Digite a forma da matriz nxm : ")
    forma = formas.split("x")
    linhas = int(forma[0])
    colunas = int(forma[1])
    matriz = np.zeros((linhas, colunas), dtype=np.float)

    for i in range(0, linhas):
        mtz = input("Digite a linha %d: " % (i+1))
        mtz = mtz.split(" ")
        for j in range(0, colunas):
            matriz[i, j] = float(mtz[j])
    return matriz

