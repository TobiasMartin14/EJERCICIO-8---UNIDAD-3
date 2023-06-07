class Personal:
    __cuil: str
    __apellido: str
    __nombre: str
    __sueldo_b: float
    __antiguedad: int
    
    def __init__(self, cuil, apellido, nombre, sueldo, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldo_b = sueldo
        self.__antiguedad = antiguedad
        
    def get_carrera(self):
        pass
    
    def getCuil(self):
        return self.__cuil
    
    def getDni(self):
        partes = self.__cuil.split("-")
        dni = partes[1]
        return dni
    
    def getApellido(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBasico(self):
        return self.__sueldo_b
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def cambiarSueldoBasico(self, nuevobasico):
        self.__sueldo_b = nuevobasico
        print("Se cambio el sueldo basico del agente ingresado.")
    
    def __str__(self):
        return self.__nombre + " " + self.__apellido + " CUIL: " + self.__cuil + " Sueldo: $" + str(self.__sueldo_b) + " antiguedad: " + str(self.__antiguedad)

    def __lt__(self, otro):
        return (self.getNombre(), self.getApellido()) < (otro.getNombre(), otro.getApellido())