from pacotes.ListaEncadeada import ListaEncadeada
import pacotes.Contato


class Pilha(ListaEncadeada):

    def deletar(self):
        self.inicioLista.estado = True
        self.inicioLista = self.inicioLista.prox
