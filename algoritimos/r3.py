def exponenciar(base,potencia):
    print(potencia)
    if potencia==0:
        return 1
    elif potencia % 2 == 0:
        metade = exponenciar(base, potencia // 2)
        return metade * metade

    return base * exponenciar(base,potencia-1)

print(exponenciar(2,100))