def procesar(cadena):
    pila = PILA()
    for c in cadena:
        if c.is_digit():
            pila.apilar(int(c))
            continue
        pila.desapilar()

    suma = 0
    while not pila.esta_vacia():
        suma += pila.desapilar()

    return suma


def insertar_ordenado(self,n):
    if not self.primero:
        return

    _nodo = NODO(n)

    if self.primero.valor > n:
        _nodo.sig = self.primero
        self.primero = _nodo
        return

    anterior = self.primero
    actual = self.primero.sig

    while actual and self.actual.valor > n:
        anterior = actual
        actual = actual.sig

    anterior.sig = _nodo
    _nodo.sig = actual

def esta_en_la_cola(cola,elemento):
    aux = COLA()
    ok = False
    while not cola.esta_vacia():
        valor = cola.desencolar()
        aux.encolar(valor)

        if valor == elemento:
            ok = True

    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

    return ok
