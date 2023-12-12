import random

def ordenacao_insercao_desc(A):
    n = len(A)
    # Percorre o arranjo A.
    for j in range(1, n):
        chave = A[j]
        i = j - 1
        # Insere o elemento A[j] na posição correta.
        while i >= 0 and A[i] < chave:  # Change the comparison here
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = chave

# Gera um arranjo aleatório para teste.
A = random.sample(range(-10, 10), 10)
print("Arranjo não ordenado: ", A)

# Chama a função ordenacao_insercao_desc para ordenar o arranjo de forma decrescente.
ordenacao_insercao_desc(A)

print("Arranjo ordenado de forma decrescente:", A)
