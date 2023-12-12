import random

def ordenacao_selecao_desc(A):
    n = len(A)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento máximo em A.
        maximo = i
        for j in range(i + 1, n):
            if A[maximo] < A[j]:  # Change the comparison here
                maximo = j
        # Coloca o elemento máximo na posição correta.
        A[i], A[maximo] = A[maximo], A[i]

# Gera um arranjo aleatório para teste.
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)

# Chama a função ordenacao_selecao_desc para ordenar o arranjo de forma decrescente.
ordenacao_selecao_desc(A)

print("Arranjo ordenado de forma decrescente:", A)
