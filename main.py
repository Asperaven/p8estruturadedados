from pacotes.Contato import Contato
from pacotes.ListaEncadeada import ListaEncadeada
from pacotes.Fila import Fila
from pacotes.Pilha import Pilha

# Cria lista encadeada

# Lista vazia
# inicioLista = None
# fimLista = None
l1 = ListaEncadeada()
l2 = Fila()
l3 = Pilha()

vazia = l1.isVazia()

print('Lista é:', vazia)

# Novo contato
c1 = Contato()
c1.nome = "Kelvin"

# Inicio da Lista
l1.adicionar(c1)
l2.enfileirar(c1)
l3.empilhar(c1)

# Criar novo contato
c2 = Contato()
c2.nome = "Richardson"

# Operacao Atualizar Lista

l1.adicionar(c2)
l2.enfileirar(c2)
l3.empilhar(c2)

# Criar novo contato
c3 = Contato()
c3.nome = "Erick"
c3.telefone = "3425"

l1.adicionar(c3)
l2.enfileirar(c3)
l3.empilhar(c3)

c5 = Contato()
c5.nome = "Joaquim"
l1.adicionar1(c5,1)
l2.enfileirar(c5)
l3.empilhar(c5)


#l1.exibir()

#l1.deletar(c5)

#l1.exibir()

l2.mostrar()

l2.desenfileirar()

l2.mostrar()

contato = l1.buscar(c3)

if contato is not None:
    print("Telefone do", contato.nome, "é:", contato.telefone)


