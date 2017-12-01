def numeros_pares(pila):
    pares = PILA()
    aux_pares = PILA()
    aux = PILA()

    while not pila.esta_vacia():
        valor = pila.desapilar()
        aux.apilar(valor)

        if valor % 2 == 0:
            aux_pares.apilar(valor)

    while not aux_pares.esta_vacia():
        pares.apilar(aux_pares.desapilar())

    while not aux.esta_vacia():
        pila.apilar(aux.desapilar())

    return pares
    
