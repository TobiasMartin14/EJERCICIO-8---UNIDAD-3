from clasePersonal import Personal

class Docente(Personal):
    __carrera: str
    __cargo: str
    __catedra: str
    
    def __init__(self, cuil = '', apellido = '', nombre = '', sueldo = 0.0, antiguedad = 0, carrera = '', cargo = '', catedra = ''):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
        
    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatedra(self):
        return self.__catedra
    
    def getSueldo(self):
        sueldotot = super().getSueldoBasico() + (super().getSueldoBasico() * (super().getAntiguedad()/100))
        if self.__cargo == "Simple":
            sueldotot += (super().getSueldoBasico() * (10/100))

        elif self.__cargo == "Semiexclusivo":
            sueldotot += (super().getSueldoBasico() * (20/100))

        elif self.__cargo == "Exclusivo":
            sueldotot += (super().getSueldoBasico() * (50/100))

        return sueldotot
    
    def cambiarPorcentaje(self, nuevoPorcentaje):
        print("El sueldo antes de cambiar el porcentaje es: {}" .format(self.getSueldo()))
        self.__extraporcargo = nuevoPorcentaje/100
        print("El sueldo con el nuevo porcentaje es: {}".format(self.getSueldo()))

    def __str__(self):
        return super().__str__() + "\nCarrera: " + self.__carrera + " Cargo: " + self.__cargo + " Catedra: " + self.__catedra