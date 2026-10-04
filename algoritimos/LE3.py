class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_no_inicio(self, dado):
        novo_no = No(dado)
        novo_no.proximo = self.cabeca
        self.cabeca = novo_no

    def buscar_valor(self,valor):
        atual = self.cabeca

        while atual is not None:
            if atual.dado == valor:
                return True
            
            atual = atual.proximo

        return False

    def append(self,valor):
        no_fim = No(valor)
        if self.cabeca == None:
            self.cabeca = no_fim
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo

            atual.proximo = no_fim

        

    def imprimir_lista(self):
        atual = self.cabeca
        elementos = []
        
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        
        print(" -> ".join(elementos) + " -> None")

        

minha_ll = ListaEncadeada()
minha_ll.adicionar_no_inicio(10)
minha_ll.adicionar_no_inicio(20)
minha_ll.adicionar_no_inicio(30)
minha_ll.append(50)
minha_ll.append(100)
minha_ll.append(22411)
print(minha_ll.imprimir_lista())