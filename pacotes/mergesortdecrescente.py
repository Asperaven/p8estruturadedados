import random

def merge(A, aux, esquerda, meio, direita):
    """
    Combina dois vetores ordenados em um único vetor (também ordenado) de forma decrescente.
    """
    for k in range(esquerda, direita + 1):
        aux[k] = A[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            A[k] = aux[j]
            j += 1
        elif j > direita:
            A[k] = aux[i]
            i += 1
        elif aux[j] > aux[i]:  # Change the comparison here
            A[k] = aux[j]
            j += 1
        else:
            A[k] = aux[i]
            i += 1


def mergesort_desc(A, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2

    # Ordena a primeira metade do arranjo.
    mergesort_desc(A, aux, esquerda, meio)

    # Ordena a segunda metade do arranjo.
    mergesort_desc(A, aux, meio + 1, direita)

    # Combina as duas metades ordenadas anteriormente.
    merge(A, aux, esquerda, meio, direita)


# Testa o algoritmo.
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)
aux = [0] * len(A)
mergesort_desc(A, aux, 0, len(A) - 1)
print("Arranjo ordenado de forma decrescente:", A)
