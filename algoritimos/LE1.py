def desinversao(lista):
    novaLista = []
    for i in range(len(lista)-1, -1,-1):
        novaLista.append(lista[i])
    return novaLista

l = [1,2,3,4,5,6]
l2 = [12,5,3,2]
print(desinversao(l2))