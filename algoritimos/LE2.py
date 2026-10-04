def remove_duplicatas(lista):
    listaFinal = []
    for i in lista:
        if i not in listaFinal:
            listaFinal.append(i)

    return listaFinal

l = ["maçã", "banana", "maçã", "pera", "banana", "uva"]
print(remove_duplicatas(l))
