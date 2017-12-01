def replicar(lista,n):
    #pre: se asume q la lista solo contiene numeros

    if not lista:
        return []

    numero = lista.pop()

    return replicar(lista,n) + [numero] * n

def palindromo(cadena):
    #pre: se asume q la cadena esta en minusculas

    if len(cadena) == 1:
        return True

    if cadena[0] == cadena[-1]:
        return palindromo(cadena[1:-1])

    return False

def pascal(fil,col):
    if col == 0 or col == fil:
        return 1

    return pascal(fil-1,col-1) + pascal(fil-1,col)
