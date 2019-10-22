import matriz as mtz
import numpy as np

escolha = int(input("(1) Para digitar.\n(2) Arqruivo *.txt .\nPor favor escolha:"))

if escolha == 1:
    A = mtz.matriz(mtz.digitar_matriz())
elif escolha == 2:
    A = mtz.matriz(mtz.txt_matriz())

print("A matriz é:\n", A)


print("Atividade 1 - Eliminação Gaussiana e Retrosubstituição")
print("Atividade 2 - Problema de Valores de Contorno")
print("Atividade 3 - Redução a forma escalonada em linha")
print("Atividade 4 - Consistência e Sistemas Homogênios")
print("Atividade 5 - Multiplicação de Matrizes")
print("Atividade 6 - Verificar se é inversível e inversa.")
atividade = int(input("Digite uma atividade:"))

if atividade == 1:
    print("A forma esclonada da matriz é:\n",np.asmatrix(A.eliminacao_gaussiana()))
    print("Os valores de X1, X2, X3:\n",A.retrosubstituicao())

elif atividade == 2:
    print(A.valoresContorno())

elif atividade == 3:
     A.escalonada_linha()

elif atividade == 4:
    A.homogeneo()
    print("\n",A)
    
elif atividade == 5:
    print("Digite matriz B")
    B = mtz.matriz(mtz.digitar_matriz())
    print(A.multiplica(B))
elif atividade == 6:
    normal, identidade = A.inv_gj()
    print(np.asmatrix(normal))
    print(np.asmatrix(identidade))
    A.origem()
    B = mtz.matriz(identidade)
    C = A.multiplica(B)
    print("A multiplicação de A por identidade é:")
    print(np.asmatrix(C))

elif atividade == 7:
    print(A.gauss_jordan())
