def achatar(lista):
    lf = []
    for e in lista:
        if isinstance(e,list):
            for a in achatar(e):
                lf.append(a)
        else:
            lf.append(e)
            
    return lf

lista = [1, [2, 3, [4, [5, 6], 7]], 8]
l2 = [1,2,3]
l3 = []
print(achatar(lista))
print(achatar(l2))
print(achatar(l3))
