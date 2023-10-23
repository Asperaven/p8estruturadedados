from pacotes.ListaEncadeada import ListaEncadeada


class Fila:
    def __init__(self):
        self.queue = ListaEncadeada()

    def enfileirar(self, item):
        self.queue.adicionar(item)

    def desenfileirar(self, item):
        if self.queue.inicioLista is not None:
            item = self.queue.inicioLista
            self.queue.inicioLista = item.prox
            return item.nome
        else:
            return None

    def mostrar(self):
        self.queue.exibir()


# Exemplo
"""minha_fila = Fila()
minha_fila.enfileirar("Item 1")
minha_fila.enfileirar("Item 2")
minha_fila.enfileirar("Item 3")"""

#print("Fila:")
#minha_fila.mostrar()  # Resultado: Item 1, Item 2, Item 3

#print("Item desinfileirado:", minha_fila.desenfileirar())  # Output: Item 1
#print("Fila após desenfileiramento:")
#minha_fila.mostrar()  # Resultado: Item 2, Item 3
