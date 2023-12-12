import random

def promove(A, filho):
    # Move o elemento para cima no heap.
    pai = (filho - 1) // 2
    while pai >= 0 and A[pai] < A[filho]:
        A[pai], A[filho] = A[filho], A[pai]
        filho = pai
        pai = (filho - 1) // 2

def demove(A, ultimo):
    # Move o elemento para baixo no heap.
    pai = 0
    filho = 1

    while filho <= ultimo:
        # Compara os filhos e escolhe o maior.
        if filho < ultimo and A[filho] < A[filho + 1]:
            filho += 1

        # Compara o maior filho com o pai.
        if A[filho] > A[pai]:
            A[pai], A[filho] = A[filho], A[pai]
            pai = filho
            filho = 2 * pai + 1
        else:
            break

def heapsort_desc(A, n):
    # Primeiro estágio: construção do heap.
    for i in range(1, n):
        promove(A, i)

    # Segundo estágio: construção da sequência ordenada.
    for i in range(n - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        demove(A, i - 1)

# Testa o algoritmo.
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)
heapsort_desc(A, len(A))
print("Arranjo ordenado de forma decrescente:", A)
