def eh_palindromo(palavra,inicio=0,fim=None):
    if fim is None:
        fim=len(palavra) -1

    if len(palavra) <= 1:
        return True
    elif palavra[inicio] != palavra[fim]:
        return False
    elif inicio == fim or inicio+1 == fim:
        return True

    return eh_palindromo(palavra,inicio +1,fim-1)

palavra = "arara"
print(eh_palindromo(palavra))


