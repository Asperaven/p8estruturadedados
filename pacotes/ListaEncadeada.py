class ListaEncadeada:
    inicioLista = None
    fimLista = inicioLista

    def adicionar(self, contato):
        if self.inicioLista is None:
            self.inicioLista = contato
        else:
            contato.prox = self.inicioLista
            self.inicioLista = contato

    def adicionar1(self, contato, ind):
        cont = 1
        ant = self.inicioLista
        aux = ant

        if (self.inicioLista is None) & ind == 1:
            self.inicioLista = contato
            contato.prox = self.fimLista
            return
        elif ind == 1:
            contato.prox = self.inicioLista
            self.inicioLista = contato
            return

        # VARREDURA
        while aux:
            ant = aux
            aux = aux.prox
            cont += 1
            if cont == ind:
                break

        # QUANDO ENCONTRA POSICAO --> INSERE
        ant.prox = contato
        contato.prox = aux

    def exibir(self):
        aux = self.inicioLista
        while aux:
            print(aux.nome)
            aux = aux.prox


    def deletar(self, contato):
        aux = self.inicioLista
        ant = aux
        while aux:
            if contato == self.inicioLista:
                self.inicioLista = contato.prox
            if aux == contato:
                ant.prox = contato.prox
            ant = aux
            aux = aux.prox

    def buscar(self, info):
        aux = self.inicioLista

        while aux:
            if (aux.nome == info) | (aux.telefone == info) | (aux == info):
                print("ACHOU! " + aux.nome)
                return aux
            elif aux.prox is None:
                print("Essa criatura não existe!")
            aux = aux.prox

    def isVazia(self):
        if self.inicioLista is None:
            ok = True
        else:
            ok = False
        return ok
