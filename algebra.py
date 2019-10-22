import numpy as np

A = np.array([[2,1,1,1],[6,2,1,-1], [-2,2,1,7]])
B = np.array([[1,2,2,3,1],[2,4,4,6,2], [1,2,4,5,3]])



def quantColun(A): # conta a quantidade de colunas de uma matriz
  colun = 0
  for i in A[0]:
    colun += 1
  return colun

def trocaLinha(matrizA, linha1, linha2): #troca as linhas de uma matriz
  for i in range( quantColun(matrizA) ):
    aux = matrizA[linha1,i]
    matrizA[linha1,i] = matrizA[linha2,i]
    matrizA[linha2,i] = aux
    
def maiorColuna(A, b, c):
  maior = A[c,b]
  linhaMaior = c 
  for i in range (c, len(A)):
    if A[i, b] > maior :
      maior = A[i,b]
      linhaMaior = i
  return linhaMaior # retorna a linha do maior numero em uma coluna
  
def pivo(A, colun):
  linha = maiorColuna(A, colun, colun) # candidato a pivo esta nessa linha
  if linha != colun : return trocaLinha(A, linha, colun)
  else: return A

def pivonaoNulo(A,linha): #procura primeira entrada não nula

  pivo = None
  aux = None
  for j in range(linha, len(A)): #percorre as linhas
    if pivo != None : break
    aux = j
    for elemento in range(linha, quantColun(A)): #percorre as colunas
      if A[j][elemento] != 0:
        pivo = elemento
        break
  if aux !=  linha:
    trocaLinha(A, linha, aux)
    
  if pivo == None : return None, None
  
  return (linha, pivo)
  
def Zerar(A, colun):
  A = pivo(A, colun) #coloca o pivo na posição correta
  quantLinhas = len(A)

  
  for i in range(colun + 1, len(A) ):
    x = A[colun][colun]/ A[i][colun]
    
    for j in range(colun, quantColun(A)):
      A[i][j] = x*A[i][j] - A[colun][j]
      
  return A

def opZerar(matriz, linhaPivo, colunaPivo):
  for i in range(linhaPivo + 1, len(matriz) ):
    if matriz[i][colunaPivo] == 0 : pass
    else :
      x = matriz[linhaPivo][colunaPivo]/ matriz[i][colunaPivo]
      for j in range(colunaPivo, quantColun(matriz)):
        matriz[i][j] = float(x*matriz[i][j] - matriz[linhaPivo][j])
        
