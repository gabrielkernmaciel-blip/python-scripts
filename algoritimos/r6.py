def caminhos(m,n):
    if m == 0 or n ==0:
        return 1

    return caminhos(m-1,n) + caminhos(m,n-1)
        
print(caminhos(3,3))