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
#l1.adicionar(c1)
#l2.adicionar(c1)
#l3.adicionar(c1)

# Criar novo contato
c2 = Contato()
c2.nome = "Richardson"

# Operacao Atualizar Lista

#l1.adicionar(c2)
#l2.adicionar(c2)
#l3.adicionar(c2)

# Criar novo contato
c3 = Contato()
c3.nome = "Erick"
c3.telefone = "3425"

#l1.adicionar(c3)
#l2.adicionar(c3)
#l3.adicionar(c3)

c4 = Contato()
c4.nome = "Joaquim"
#l1.adicionar(c4)
#l2.adicionar(c4)
#l3.adicionar(c4)

"""print("Mostrar antes de deletar")
l1.exibir()
l1.deletar(c5)
print("Mostrar depois de deletar")
l1.exibir()"""

"""print("Mostrar primeiro")
l2.exibir()
l2.deletar()
print("Mostrar segundo")
l2.exibir()
l2.deletar()
print("Mostrar terceiro")
l2.exibir()"""

"""print("Mostrar antes de desempilhar")
l3.exibir()
l3.deletar()
print("Mostrar depois de desempilhar")
l3.exibir()"""

#contato = l1.buscar(c3)

#if contato is not None:
    #print("Telefone do", contato.nome, "é:", contato.telefone)


