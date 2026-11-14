import math

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

dados = {
    "Cliente": ["A", "B", "C", "D", "E"],
    "Idade": [20, 25, 40, 55, 70],
    "Renda": [2000, 3000, 6000, 9000, 12000],
}
df = pd.DataFrame(dados)

a_original = [df.loc[0, "Idade"], df.loc[0, "Renda"]]
b_original = [df.loc[1, "Idade"], df.loc[1, "Renda"]]
distancia_original = math.dist(a_original, b_original)

print("Valores originais:")
print(df)
print(f"\nDistancia A-B com valores originais: {distancia_original}")

scaler = MinMaxScaler()
df_normalizado = df.copy()
df_normalizado[["Idade", "Renda"]] = scaler.fit_transform(df[["Idade", "Renda"]])

print("\nValores normalizados:")
print(df_normalizado)

a_normalizado = [
    df_normalizado.loc[0, "Idade"],
    df_normalizado.loc[0, "Renda"],
]
b_normalizado = [
    df_normalizado.loc[1, "Idade"],
    df_normalizado.loc[1, "Renda"],
]
distancia_normalizada = math.dist(a_normalizado, b_normalizado)

print(f"\nDistancia A-B com valores normalizados: {distancia_normalizada}")

print(
    f"\nComparacao: a distancia caiu de {distancia_original:.2f} para "
    f"{distancia_normalizada:.4f}, ou seja, a normalizacao reduziu o valor em "
    f"{distancia_original - distancia_normalizada:.2f}."
)

# A renda domina a distancia quando os valores originais sao usados porque a
# distancia Euclidiana soma quadrados de diferencas na unidade original de cada
# atributo. A diferenca de renda entre A e B e de 1000 reais, enquanto a
# diferenca de idade e de apenas 5 anos. Como 1000^2 = 1.000.000 e 5^2 = 25, o
# termo da renda e 40.000 vezes maior que o da idade, entao a idade praticamente
# nao influencia o resultado. Depois da normalizacao Min-Max as duas colunas
# passam a variar no mesmo intervalo (0 a 1), e cada atributo contribui de forma
# comparavel para a distancia final.
print(
    "\nPor que a renda influencia muito mais com os valores originais: a "
    "distancia soma quadrados de diferencas na unidade original de cada "
    "atributo. A diferenca de renda (1000) ao quadrado vale 1.000.000, enquanto "
    "a diferenca de idade (5) ao quadrado vale 25, ou seja, a renda pesa 40.000 "
    "vezes mais. A normalizacao Min-Max coloca as duas colunas no intervalo de "
    "0 a 1, deixando os atributos comparaveis."
)
