def mesclar(lista1, lista2):
    if len(lista1) == 0:
        return lista2 
    if len(lista2) == 0:
        return lista1       

    if lista1[0] <= lista2[0]:
        v = lista1.pop(0)
    else:
        v = lista2.pop(0)

    resto = mesclar(lista1, lista2)

    return [v] + resto
  
    
print(mesclar([1,3,5], [2,4,6]))

