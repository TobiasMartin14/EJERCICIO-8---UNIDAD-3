from zope.interface import Interface

class IColeccion(Interface):

    def insertarElemento(self, objeto, posicion):
        pass

    def agregarElemento(self, objeto):
        pass

    def mostrarElemento(self, posicion):
        pass
