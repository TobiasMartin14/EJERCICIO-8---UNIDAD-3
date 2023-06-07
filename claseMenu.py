from claseManejador import ManejadorAgente
from claseNodo import Nodo
from clasePersonal import Personal
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador

class Menu:
    __cod: int
    
    def __init__(self):
        self.__cod = 0
    
    def mostrar_menu(self):
        print('')
        print('Opcion 1: Cargar Agentes del archivo')
        print('Opcion 2: Crear e insertar un agente a la coleccion')
        print('Opcion 3: Crear y agregar un agente al final de la coleccion')
        print('Opcion 4: Dada una posicion de la colección, mostrar que tipo de agente se encuentra')
        print('Opcion 5: Dada una carrera, mostrar un listado ordenado por nombre de todos los Docentes Investigadores')
        print('Opcion 6: Dada un area de investigacion mostrar cuantos son Investigadores y cuantos son Docentes Investigadores')
        print('Opcion 7: Mostrar Nombre, Apellido, tipo de agente y sueldo de todos los agentes ordenado por apellido')
        print('Opcion 8: Dada una categoria de Investigacion generar un listado')
        print('Opcion 9: Tesorero: acceder a los gastos que la universidad tiene en concepto de sueldos')
        print('Opcion 10: Abrir menu de opciones para Director')
        print('Opcion 11: Guardar la coleccion en el archivo "personal.json"')
        print('Opcion 0: Finalizar Operacion')
        print('')
        print('--------------------------------------------------------------------------------------------------------')
        
        
    def ejecutar_menu(self, MA:ManejadorAgente):
        self.mostrar_menu()
        self.__cod = int(input('Ingrese el Codigo'))
        while self.__cod != 0:
            if self.__cod == 1:
                MA.cargar()
            elif self.__cod == 2:
                unAgente = MA.crear_personal()
                MA.insertarElemento(unAgente)
            elif self.__cod == 3:
                unAgente = MA.crear_personal()
                MA.agregarElemento(unAgente)
            elif self.__cod == 4:
                MA.mostrar_tipo_posicion()
            elif self.__cod == 5:
                MA.generar_listado_carrera()
            elif self.__cod == 6:
                area = input("Ingrese un area de investigacion: ")
                MA.contar_area(area)
            elif self.__cod == 7:
                MA.listado_agentes()
            elif self.__cod == 8:
                MA.listar_segun_categoria()
            elif self.__cod == 9:
                print("INICIAR SESION")
                usuario = str(input("Ingrese el nombre de usuario: "))
                contrasena = str(input("Ingrese la contrasena: "))

                if usuario == "uTesorero" and contrasena == "ag@74ck":
                    dni = str(input("Ingrese el dni de un empleado: "))
                    band = MA.verificarDni(dni)
                    if band:
                        MA.gastosSueldoPorEmpleado(dni)
                    else:
                        print("El dni ingreasdo no corresponde a un")
                    
                else:
                        print("El DNI ingresado no corresponde a ningun empleado registrado")
                        
            elif self.__cod == 10:
                
                print("INICIAR SESION")
                usuario = str(input("Ingrese el nombre de usuario: "))
                contrasena = str(input("Ingrese la contrasena: "))

                if usuario == "uDirector" and contrasena == "ufC77#!1":
                    print("MENU DE OPCIONES DE DIRECTOR: ")
                    oplocal = 0
                    while oplocal != 5:
                        print("1: Modificar sueldo basico de un agente.")
                        print("2: Modificar porcentaje por cargo de un docente.")
                        print("3: Modificar porcentaje por categoria de personal de apoyo.")
                        print("4: Modificar importe extra de docente investigador.")
                        print("5: Salir.")
                        oplocal = int(input("Ingrese una opcion: "))
                        dni = str(input("Ingrese el dni de un empleado: "))

                        if oplocal == 1:
                            
                            band = MA.verificarDni(dni)
                            
                            if band == True:
                                nuevobasico = float(input("Ingrese el nuevo sueldo basico del agente: "))
                                MA.modificarBasico(dni, nuevobasico)
                            else:
                                print("El DNI ingresado no corresponde a ningun empleado registrado")

                        elif oplocal == 2:

                            band = MA.verificarDocente(dni)

                            if band == True:
                                nuevoPorcentaje = int(input("Ingrese el nuevo porcentaje: "))
                                MA.modificarPorcentajeporcargo(dni, nuevoPorcentaje)
                            else:
                                print("El DNI ingresado no corresponde a ningun Docente registrado.")


                        elif oplocal == 3:

                            band = MA.verificarPersonalDeApoyo(dni)

                            if band == True:
                                nuevoPorcentaje = int(input("Ingrese el nuevo porcentaje: "))
                                MA.modificarPorcentajeporcategoria(dni, nuevoPorcentaje)
                            else:
                                print("El DNI ingresado no corresponde a ningun Personal de Apoyo registrado.")

                        elif oplocal == 4:

                            band = MA.verificarDocenteInvestigador(dni)

                            if band == True:
                                nuevoImporteExtra = float(input("Ingrese el nuevo importe extra: "))
                                MA.modificarImporteExtra(dni, nuevoImporteExtra)
                            else:
                                print("El DNI ingresado no corresponde a ningun Docente Investigador registrado.")

                        else:
                            print("Salio del menu de director")

                else:
                    print("Usuario y/o contrasena incorrectos ")
            self.mostrar_menu()
            self.__cod = int(input('Ingrese el Codigo'))