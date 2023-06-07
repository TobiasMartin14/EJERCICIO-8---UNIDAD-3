from claseDocente import Docente
from claseInvestigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoria_programa: str
    __extra: float
    
    def __init__(self, cuil = '', apellido = '', nombre = '', sueldo = 0.0, antiguedad = 0, area = '', tipo = '', carrera = '', cargo = '', catedra = '', categoria_programa = '', extra = 0.0):
        Docente.__init__(self, cuil, apellido, nombre, sueldo, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldo, antiguedad, area, tipo)
        self.__categoria_programa = categoria_programa
        self.__extra = extra
        
    def get_carrera(self):
        return super().get_carrera()

    def getCategoria(self):
        return self.__categoria_programa
    
    def getExtra(self):
        return self.__extra
    
    def getSueldo(self):
        
        sueldoDocente = super(Docente,self).getSueldo()
        sueldotot =  sueldoDocente + self.__extra
        
        return sueldotot
    
    def cambiarImporteExtra(self, nuevoExtra):
        self.__extra = nuevoExtra
        print("Se modifico el importe extra que recibe el docente investigador.")

    def __str__(self):
        return super().__str__() + "\n Categoria: " + self.__categoria_programa + " Importe extra por docencia e investigacion: $" + str(self.__extra)
    
    def __lt__(self, otro):
        return super().getNombre() < otro.getNombre()