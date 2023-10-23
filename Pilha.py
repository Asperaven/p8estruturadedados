from pacotes.ListaEncadeada import ListaEncadeada


class Pilha:
    def __init__(self):
        self.stack = ListaEncadeada()

    def empilhar(self, item):
        self.stack.adicionar(item)

    def desempilhar(self):
        if self.stack.inicioLista:
            item = self.stack.inicioLista
            self.stack.inicioLista = item.prox
            return item.nome
        else:
            return None

    def mostrar(self):
        self.stack.exibir()


# Exemplo
"""minha_pilha = Pilha()
minha_pilha.empilhar("Item 1")
minha_pilha.empilhar("Item 2")
minha_pilha.empilhar("Item 3")"""

#print("Pilha:")
#minha_pilha.mostrar()  # Resultado: Item 1, Item 2, Item 3

#print("Item desempilhado:", minha_pilha.desempilhar())  # Resultado: Item 3
#print("Pilha depois do desempilhamento:")
#minha_pilha.mostrar()  # Output: Item 1, Item 2
