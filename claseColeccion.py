from zope.interface import implementer
from coleccionInterfaz import IColeccion
from DirectorInterfaz import IDirector
from TesoreroInterfaz import ITesorero
from claseNodo import Nodo
from clasePersonal import Personal
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador

@implementer(IColeccion)
@implementer (IDirector)
@implementer (ITesorero)
class Coleccion:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
        self.__tope = 0
        self.__indice = 0
        
    def __iter__(self):
        self.__actual = self.__comienzo
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.get_dato()
            self.__actual = self.__actual.get_siguiente()
            return dato
    
    def insertarElemento(self, unPersonal: Personal, posicion):
        unNodo = Nodo(unPersonal)
        if posicion == 0:
            aux = self.__comienzo
            self.__comienzo = unNodo
            self.__comienzo.set_siguiente(aux)
            self.__tope += 1
        else:
            i = 0
            anterior = self.__comienzo
            posterior = self.__comienzo
            while i < posicion and posterior.get_siguiente() != None:
                anterior = posterior
                posterior = posterior.get_siguiente()
                i += 1
            if posterior == None:
                anterior.set_siguiente(unNodo)
                self.__tope += 1
            else: 
                anterior.set_siguiente(unNodo)
                unNodo.set_siguiente(posterior)
                self.__tope += 1
        
    def agregarElemento(self, unPersonal: Personal):
        unNodo = Nodo(unPersonal)
        if self.__comienzo == None:
            self.__comienzo = unNodo
            self.__tope += 1
        else:
            aux = self.__comienzo
            while aux.get_siguiente() != None:
                aux = aux.get_siguiente()
            aux.set_siguiente(unNodo)
            self.__tope += 1

    def mostrar_posicion_tipo(self, posicion):
        if posicion == 0:
            print(self.__comienzo)
        else:
            i = 0
            aux = self.__comienzo
            while i < posicion and aux.get_siguiente() != None:
                aux = aux.get_siguiente()
                i += 1
            if posicion == i:
                unPersonal = aux.get_dato()
                if isinstance(unPersonal, Apoyo):
                    print('Es un agente de Apoyo')
                elif isinstance(unPersonal, Docente):
                    print('Es un Docente')
                elif isinstance(unPersonal, Investigador):
                    print('Es un investigador')
                elif isinstance(unPersonal, DocenteInvestigador):
                    print('Es un Docente Investigador')
                    
    def listadoDocentesInvestigadores(self, ingcarrera):
        aux = self.__comienzo
        listaordenada = []
        while aux != None:
            if(aux.getDatoCarrera() == ingcarrera):
                listaordenada.append(aux.get_dato())
            aux = aux.get_siguiente()

        listaordenada.sort()
        for docenteinvestigador in listaordenada:
            print(docenteinvestigador)

    def contarArea(self, area):
        aux = self.__comienzo
        contDocenteInvestigador = 0
        contInvestigador = 0
        while aux != None:
            if (aux.getDatoArea() == area):
                if(aux.esDocInvestigador()):
                    contDocenteInvestigador += 1
                elif (aux.esInvestigador()):
                    contInvestigador += 1
            aux = aux.get_siguiente()

        print("El area de investigacion {} tiene {} docente/s investigador/es, y {} investigador/es".format(area, contDocenteInvestigador,contInvestigador))


    def listadoAgentes(self):
        aux = self.__comienzo
        listaAgentes = []

        while aux != None:
            agente = aux.getAgente()
            listaAgentes.append(agente)
            aux = aux.get_siguiente()

        listaAgentes.sort()

        for agente in listaAgentes:
            print(agente)

    
    def listarSegunCategoria(self, ingcat):
        importeSecretaria = 0
        aux = self.__comienzo

        while aux != None:
            if  aux.esDocInvestigador():
                if aux.getDatoCategoria() == ingcat:
                    aux.mostrarDocInvestigador()
                    importeSecretaria += aux.getDatoImporteExtra()
            aux = aux.get_siguiente()
        print("El importe total que debe solicitar la Secreteria de Investigacion al Ministerio es: {}".format(importeSecretaria))

    def verificarDni(self,ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
            aux = aux.get_siguiente()

        return band

    def gastosSueldoPorEmpleado(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
                print("El sueldo del empleado ingresado es: {}".format(aux.getDatoSueldo()))
            aux = aux.get_siguiente()


    def modificarBasico(self, ingdni, nuevobasico):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni:
                band = True
                aux.modificarSueldoBasico(nuevobasico)
            aux = aux.get_siguiente()
    
    def verificarDocente(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocente() == True:
                band = True
            aux = aux.get_siguiente()

        return band 

    def modificarPorcentajeporcargo(self, ingdni, nuevoPorcentaje):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocente() == True:
                band = True
                aux.modificarPorcentaje(nuevoPorcentaje)
            aux = aux.get_siguiente()

    def verificarPersonalDeApoyo(self,ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esPersonalDeApoyo() == True:
                band = True
            aux = aux.get_siguiente()
        return band 

    def modificarPorcentajeporcategoria(self,ingdni, nuevoPorcentaje):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esPersonalDeApoyo() == True:
                band = True
                aux.modificarPorcentaje(nuevoPorcentaje)
            aux = aux.get_siguiente()

    def verificarDocenteInvestigador(self, ingdni):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocInvestigador() == True:
                band = True
            aux = aux.get_siguiente()

        return band

    def modificarImporteExtra(self, ingdni, nuevoImporteExtra):
        aux = self.__comienzo
        band = False
        while aux != None and band == False:
            if aux.getDatoDni() == ingdni and aux.esDocInvestigador() == True:
                band == True
                aux.modificarExtra(nuevoImporteExtra)
            aux = aux.get_siguiente()
