aluno_a = [8.0, 92, 10]
aluno_b = [7.8, 90, 9]
aluno_c = [5.2, 68, 3]


def distancia_euclidiana(p, q):
    """Distancia Euclidiana calculada manualmente, sem funcoes prontas."""
    soma = 0
    for valor_p, valor_q in zip(p, q):
        diferenca = valor_p - valor_q
        soma = soma + diferenca ** 2
    return soma ** 0.5


distancia_ab = distancia_euclidiana(aluno_a, aluno_b)

distancia_ac = distancia_euclidiana(aluno_a, aluno_c)

print(f"Aluno A: {aluno_a}")
print(f"Aluno B: {aluno_b}")
print(f"Aluno C: {aluno_c}")
print(f"\nDistancia A-B: {distancia_ab}")
print(f"Distancia A-C: {distancia_ac}")

if distancia_ab < distancia_ac:
    mais_proximo = "B"
else:
    mais_proximo = "C"

print(f"\nAluno mais proximo de A: {mais_proximo}")

# A mesma logica usada em duas dimensoes vale para tres atributos: o laco percorre
# os tres atributos do vetor, entao nao foi preciso escrever uma formula nova.
# Basta incluir mais um par (valor_p - valor_q) ** 2 dentro da soma; a raiz
# quadrada do total continua sendo a distancia Euclidiana no espaco de tres
# dimensoes.
