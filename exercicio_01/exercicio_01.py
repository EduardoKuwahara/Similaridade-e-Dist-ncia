import math

cliente_a = [25, 2]
cliente_b = [28, 6]

diferenca_idade = cliente_a[0] - cliente_b[0]

diferenca_compras = cliente_a[1] - cliente_b[1]

quadrado_idade = diferenca_idade ** 2
quadrado_compras = diferenca_compras ** 2

soma = quadrado_idade + quadrado_compras

distancia = math.sqrt(soma)

print(f"Cliente A: {cliente_a}")
print(f"Cliente B: {cliente_b}")
print(f"Diferenca de idade: {diferenca_idade}")
print(f"Diferenca de compras: {diferenca_compras}")
print(f"Quadrado da diferenca de idade: {quadrado_idade}")
print(f"Quadrado da diferenca de compras: {quadrado_compras}")
print(f"Soma dos quadrados: {soma}")
print(f"Distancia Euclidiana entre A e B: {distancia}")
