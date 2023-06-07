import json
from claseDecodificador import Decodificador
from claseColeccion import Coleccion
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador



class ManejadorAgente:
    __personal: Coleccion
    
    def __init__(self):
        self.__personal = Coleccion()
        
    def cargar(self):
        jsonF = Decodificador()
        diccionario = jsonF.leerJSON('personal.json')
        self.__personal = jsonF.decodificarDic(diccionario)
        
    def crear_personal(self):
        print('Ingrese los siguientes datos:')
        cuil = input('CUIL: (formato: XX-XXXXXXXX-X)')
        apellido = input('Apellido')
        nombre = input('Nombre')
        sueldo_b = float(input('Sueldo base'))
        antiguedad = int(input('Antigüedad'))
        tipo = input('Tipo de Personal ("Apoyo", "Docente", "Investigador", "DocenteInvestigador")')
        if tipo == "Apoyo":
            cat = int(input('Categoria'))
            unPersonal = Apoyo(cuil, apellido, nombre, sueldo_b, antiguedad, cat)
        elif tipo == "Docente":
            carrera = input('Carrera')
            cargo = input('Cargo')
            catedra = input('Catedra')
            unPersonal = Docente(cuil, apellido, nombre, sueldo_b, antiguedad, carrera, cargo, catedra)
        elif tipo == "Investigador":
            area = input('Area de investigacion')
            tipo = input('Tipo de investigacion')
            unPersonal = Investigador(cuil, apellido, nombre, sueldo_b, antiguedad, area, tipo)
        elif tipo == "DocenteInvestigador":
            area = input('Area de investigacion')
            tipo = input('Tipo de investigacion')
            carrera = input('Carrera')
            cargo = input('Cargo')
            catedra = input('Catedra')
            cat = input('Categoría en el programa de incentivos de investigación')
            extra = float(input('Importe extra por docencia e investigación'))
            unPersonal = DocenteInvestigador(cuil, apellido, nombre, sueldo_b, antiguedad, area, tipo, carrera, cargo, catedra, cat, extra)
        else:
            print('El tipo ingresado es incorrecto')
        return unPersonal
    
    def insertarElemento(self, Agente):
        posicion = int(input('Ingrese la posicion a insertar el Agente'))
        self.__personal.insertarElemento(Agente, posicion)
        
    def agregarElemento(self, Agente):
        self.__personal.agregarElemento(Agente)
        
    def mostrar_tipo_posicion(self):
        posicion = int(input('Ingrese la posicion a mostrar el tipo de agente'))
        self.__personal.mostrar_posicion_tipo(posicion)
        
    def generar_listado_carrera(self):
        carrera = input('Ingrese el nombre de la carrera a realizar listado de los Docentes Investigadores')
        self.__personal.listadoDocentesInvestigadores(carrera)
        
    def contar_area(self, area):
        self.__personal.contarArea(area)
        
    def listado_agentes(self):
        self.__personal.listadoAgentes()
        
    def listar_segun_categoria(self):
        cat = input("Ingrese una categoria de investigacion (I, II, III, IV o V): ")
        self.__personal.listarSegunCategoria(cat)
        
    def gastosSueldoPorEmpleado(self, dni):
        self.__personal.gastosSueldoPorEmpleado(dni)
        
    def verificarDni(self, dni):
        return self.__personal.verificarDni(dni)
    
    def modificarBasico(self, dni, nuevobasico):
        self.__personal.modificarBasico(dni, nuevobasico)
        
    def verificarDocente(self, dni):
        return self.__personal.verificarDocente(dni)
        
    def verificarPersonalDeApoyo(self, dni):
        return self.__personal.verificarPersonalDeApoyo(dni)
        
    def verificarDocenteInvestigador(self, dni):
        return self.__personal.verificarDocenteInvestigador(dni)
    
    def modificarPorcentajeporcargo(self, dni, nuevo):
        self.__personal.modificarPorcentajeporcargo(dni, nuevo)
        
    def modificarPorcentajeporcategoria(self, dni, nuevo):
        self.__personal.modificarPorcentajeporcategoria(dni, nuevo)
        
    def modificarImporteExtra(self, dni, nuevo):
        self.__personal.modificarImporteExtra(dni, nuevo)
        
    

            
        