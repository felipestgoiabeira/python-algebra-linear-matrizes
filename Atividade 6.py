import matriz as mtz
from sympy import *

A = mtz.matriz(mtz.txt_matriz())


def nao_singular(A):
    det = A.determinante()
    if det != 0: return True
    else : return False
identidade = A.identidade()
print(identidade)

