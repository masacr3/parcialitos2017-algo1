def promedio(cola):
    aux = Cola()
    items = 0
    sumar = 0

    while not cola.esta_vacia():
        contador += 1
        valor = cola.desencolar()
        aux.encolar(valor)
        sumar += valor

    #evitamos el ZERODIVISIONERRROR
    if not items:
        return 0

    #acomodamos la cola como estaba
    while not aux.esta_vacia():
        cola.encolar(aux.desencolar())

    #promedio
    return sumar/items

def remover_todos(self,elemento):

    if not self.primero:
        return

    if self.primero.valor == elemento:
        self.primero = self.primero.sig

    anterior = self.primero
    actual = self.primero.sig

    while actual:
        if actual.valor == elemento:
            actual = actual.sig
            anterior.sig = actual
            continue

        anterior = actual
        actual = actual.sig
