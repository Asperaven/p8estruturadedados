import random

def mediana_de_tres(A, i, j, k):
    # Retorna o índice da mediana de três elementos.
    if A[i] < A[j]:
        return j if A[j] < A[k] else k
    else:
        return i if A[i] < A[k] else k

def particao(A, esquerda, direita):
    # Particiona o arranjo em relação ao pivô.
    i = esquerda + 1
    j = direita
    pivo = esquerda

    while True:
        while i <= j and A[i] >= A[pivo]:
            i += 1
        while i <= j and A[j] <= A[pivo]:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break

    A[pivo], A[j] = A[j], A[pivo]
    return j

def quicksort_desc(A, esquerda, direita):
    if esquerda >= direita:
        return

    # Calcula a mediana de três elementos.
    m = mediana_de_tres(A, esquerda, (direita - esquerda) // 2, direita)
    # Usa a mediana calculada como pivô.
    A[esquerda], A[m] = A[m], A[esquerda]

    indice_pivo = particao(A, esquerda, direita)
    quicksort_desc(A, esquerda, indice_pivo - 1)
    quicksort_desc(A, indice_pivo + 1, direita)

# Testa o algoritmo.
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)
quicksort_desc(A, 0, len(A) - 1)
print("Arranjo ordenado de forma decrescente:", A)
