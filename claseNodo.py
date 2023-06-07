from clasePersonal import Personal
from claseDocente import Docente
from claseApoyo import Apoyo
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador

class Nodo:
    __agente: Personal
    __siguiente: object
    
    def __init__(self, objeto:Personal):
        self.__agente = objeto
        self.__siguiente = None
        
    def set_siguiente(self, siguiente:Personal):
        self.__siguiente = siguiente
        
    def get_siguiente(self):
        return self.__siguiente
    
    def get_dato(self):
        return self.__agente
    
    def getDatoCarrera(self):
        return self.__agente.get_carrera()
    
    def getTipo(self):
        
        if isinstance(self.__agente, Docente):
            print("Docente")
        elif isinstance(self.__agente, DocenteInvestigador):
            print("Docente Investigador")
        elif isinstance(self.__agente, Apoyo):
            print("Personal de apoyo")
        elif isinstance(self.__agente, Investigador):
            print("Investigador")

    def getDatoCarrera(self):
        if isinstance(self.__agente, Docente) or isinstance(self.__agente, DocenteInvestigador):
            return self.__agente.getCarrera()
        else: 
            return False
        
    def getDatoArea(self):
        if isinstance(self.__agente, DocenteInvestigador) or isinstance(self.__agente, Investigador):
            return self.__agente.getArea()
        else:
            return False
        
    def getDatoDni(self):
        return self.__agente.getDni()
    
    def esInvestigador(self):
        return isinstance(self.__agente, Investigador)
    
    def esDocInvestigador(self):
        return isinstance(self.__agente, DocenteInvestigador)
    
    def esDocente(self):
        return isinstance(self.__agente, Docente)
    
    def esPersonalDeApoyo(self):
        return isinstance(self.__agente, Apoyo)
    
    def getAgente(self):
        cadena = self.__agente.getNombre() + " " + self.__agente.getApellido() + " "
        if isinstance(self.__agente,DocenteInvestigador):
            cadena += "Docente Investigador $" 
        elif isinstance(self.__agente, Docente):
            cadena += "Docente $"
        elif isinstance(self.__agente, Investigador):
            cadena += "Investigador $"
        elif isinstance(self.__agente, Apoyo):
            cadena += "Personal de Apoyo $"   
        
        cadena += str(self.__agente.getSueldo())

        return cadena

    def getDatoCategoria(self):
        return self.__agente.getCategoria()

    def mostrarDocInvestigador(self):
        print("{} {} \tImporte Extra por docencia e investigacion: {}".format(self.__agente.getApellido(),self.__agente.getNombre(), self.__agente.getExtra()))

    def getDatoImporteExtra(self):
        return self.__agente.getExtra()
    
    def getDatoSueldo(self):
        return self.__agente.get_sueldo()
    
    def modificarSueldoBasico(self,nuevobasico):
        self.__agente.cambiarSueldoBasico(nuevobasico)

    def modificarPorcentaje(self,nuevoporcentaje):
        self.__agente.cambiarPorcentaje(nuevoporcentaje)

    def modificarExtra(self,nuevoImporteExtra):
        self.__agente.cambiarImporteExtra(nuevoImporteExtra)