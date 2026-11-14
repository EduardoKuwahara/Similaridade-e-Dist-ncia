import math

clientes = {
    "A": [25, 2],
    "B": [27, 3],
    "C": [30, 5],
    "D": [45, 10],
    "E": [52, 12],
}


distancias = {
    nome: math.dist(clientes["A"], valores)
    for nome, valores in clientes.items()
    if nome != "A"
}

for nome, distancia in distancias.items():
    print(f"Distancia A-{nome}: {distancia}")

cliente_mais_proximo = min(distancias, key=distancias.get)

print(
    f"\nO cliente {cliente_mais_proximo} possui o perfil mais proximo de A "
    f"considerando idade e compras por mes."
)
