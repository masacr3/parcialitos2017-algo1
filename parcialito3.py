#ejercicio 1
def eliminar_consecutivos(self):
    if not self.primero or not self.primero.sig:
        return

    actual = self.primero
    camino = self.primero.sig

    while camino:

        if actual.dato == camino.dato:
            actual.sig = camino
            camino = camino.sig
            continue

        actual = camino
        camino = camino.sig

#ejercicio 2
def swap_pilas(pila1,pila2):
    aux,aux2 = Pilas()

    while not pila1.esta_vacia():
        aux.apilar(pila1.desapilar())

    while not pila2.esta_vacia():
        aux2.apilar(pila2.desapilar())

    while not aux.esta_vacia():
        pila2.apilar(aux.desapilar)

    while not aux2.esta_vacia():
        pila1.apilar(aux2.desapilar())


#ejercicio 3

def prioriazar_nombres_con_M(lista):
    #pre: lista -> cola

    lista_m , lista_sin_m = Cola()

    while not lista.esta_vacia():

        nombre = lista.desencolar().lower()

        if nombre[0] == 'm':
            lista_m.encolar(nombre)
            continue

        lista_sin_m.encolar(nombre)

    while not lista_m.esta_vacia():
        lista.encolar(lista_m.desencolar())

    while not lista_sin_m.esta_vacia():
        lista.encolar(lista_sin_m.desencolar)
