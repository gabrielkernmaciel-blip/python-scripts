class No:
    def __init__(self,dado):
        self.dado = dado
        self.prox = None

class ListaEncadeada:
    def __init__(self):
        self.primeiro = None

    def adicionar_primeiro(self,valor):
        novo_no = No(valor)
        novo_no.prox = self.primeiro
        self.primeiro = novo_no

    def printar_lista(self):
        atual = self.primeiro
        impressora = []
        while atual is not None:
            impressora.append(str(atual.dado))
            atual = atual.prox

        print(" -> ".join(impressora) + " -> None")

lista_principal = ListaEncadeada()
lista_principal.adicionar_primeiro(50)
lista_principal.adicionar_primeiro(10)
lista_principal.adicionar_primeiro(11)
lista_principal.printar_lista()