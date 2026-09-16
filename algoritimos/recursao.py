def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)

print(fatorial(6))

def soma_recursiva(lista,indice=0):
    if indice == len(lista):
        return 0
    return lista[indice] + soma_recursiva(lista,indice + 1)

listaTeste = [0,1,2,3,4,5]
print(soma_recursiva(listaTeste))