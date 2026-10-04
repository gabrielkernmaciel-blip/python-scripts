def formas(n):
    if n <= 1:
        return 1 

    return  formas(n-1) + formas(n-2)

    

print(formas(10))