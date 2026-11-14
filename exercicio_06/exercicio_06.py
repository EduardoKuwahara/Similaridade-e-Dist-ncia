import math

import pandas as pd

registros = {
    "A": [1, 1],
    "B": [4, 5],
    "C": [2, 2],
    "D": [5, 4],
}

nomes = list(registros)

matriz = pd.DataFrame(index=nomes, columns=nomes, dtype=float)

for nome_i in nomes:
    for nome_j in nomes:
        matriz.loc[nome_i, nome_j] = math.dist(registros[nome_i], registros[nome_j])

print("Matriz de distancias:")
print(matriz)

menor_distancia = None
par_mais_proximo = None

for nome_i in nomes:
    for nome_j in nomes:
        if nome_i == nome_j:
            continue
        valor = matriz.loc[nome_i, nome_j]
        if menor_distancia is None or valor < menor_distancia:
            menor_distancia = valor
            par_mais_proximo = (nome_i, nome_j)

print(f"\nMenor distancia diferente de zero: {menor_distancia}")
print(f"Par de registros mais proximo: {par_mais_proximo}")

# existe empate. A-C e B-D valem a mesma distancia (raiz de 2), porque
# A e C diferem em 1 unidade nos dois atributos, e B e D tambem. O laco percorre
# as linhas em ordem alfabetica e, usando < (estritamente menor), mantem o
# primeiro par encontrado, que e A-C.

diagonal_zerada = all(matriz.loc[nome, nome] == 0 for nome in nomes)
print(f"\nDiagonal principal apenas com zeros: {diagonal_zerada}")

simetrica = all(
    matriz.loc[nome_i, nome_j] == matriz.loc[nome_j, nome_i]
    for nome_i in nomes
    for nome_j in nomes
)
print(f"Matriz simetrica: {simetrica}")

# A diagonal e zero porque a distancia de um registro ate ele mesmo e sempre 0:
# a diferenca de cada atributo consigo mesmo e 0, e a raiz quadrada da soma de
# zeros tambem e 0. A matriz e simetrica porque d(A,B) = d(B,A): a formula da
# distancia Euclidiana eleva ao quadrado a diferenca entre os atributos, e
# (a - b)^2 e igual a (b - a)^2. Trocar a ordem dos registros nao muda o
# resultado, apenas a ordem em que os termos aparecem na soma.
