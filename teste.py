import matriz as mtz
A = mtz.matriz(mtz.txt_matriz())
G, pivos, rank = A.escalonada_linha()
colunas_basicas = [pivo[1] for pivo in pivos]
colunas_livres = [x for x in range(A.colunas) if not x in colunas_basicas]




naozeros = A.dois_naozero()

lista = A.lista_linha(naozeros[0][0])

print(A.linhas)
print(lista)
