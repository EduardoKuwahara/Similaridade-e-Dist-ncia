cliente_a = [25, 2]
cliente_b = [27, 3]
cliente_c = [45, 10]
cliente_d = [52, 12]


def distancia_euclidiana(p, q):
    """Distancia Euclidiana calculada manualmente, sem funcoes prontas."""
    soma = 0
    for valor_p, valor_q in zip(p, q):
        diferenca = valor_p - valor_q
        soma = soma + diferenca ** 2
    return soma ** 0.5


distancia_ab = distancia_euclidiana(cliente_a, cliente_b)

distancia_ac = distancia_euclidiana(cliente_a, cliente_c)

distancia_ad = distancia_euclidiana(cliente_a, cliente_d)

distancias = {
    "B": distancia_ab,
    "C": distancia_ac,
    "D": distancia_ad,
}

cliente_mais_proximo = min(distancias, key=distancias.get)

print(f"Distancia A-B: {distancia_ab}")
print(f"Distancia A-C: {distancia_ac}")
print(f"Distancia A-D: {distancia_ad}")
print(f"\nCliente mais proximo de A: {cliente_mais_proximo}")

# A menor distancia indica maior semelhanca porque a distancia Euclidiana mede o
# quanto dois registros estao afastados no espaco dos atributos usados (idade e
# compras por mes). Como ambos os atributos estao na mesma ordem de grandeza,
# somar os quadrados das diferencas faz com que qualquer afastamento em qualquer
# atributo aumente o valor final. Assim, quanto menores as diferencas de idade e
# de compras entre dois clientes, menor a distancia entre eles - e menor
# distancia significa comportamento mais parecido. O cliente B difere de A em
# apenas 2 anos e 1 compra, enquanto C difere em 20 anos e 8 compras e D em 27
# anos e 10 compras, por isso B e o mais semelhante.
