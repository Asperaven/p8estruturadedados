from pacotes.ListaEncadeada import ListaEncadeada
import pacotes.Contato


class Fila(ListaEncadeada):

    def adicionar(self, contato):
        if self.fimLista is None:
            self.inicioLista = contato
            self.fimLista = contato
            contato.prox = None
        else:
            self.fimLista.prox = contato
            self.fimLista = contato
            contato.prox = None


    def deletar(self):
        self.inicioLista.estado = True
        self.inicioLista = self.inicioLista.prox

