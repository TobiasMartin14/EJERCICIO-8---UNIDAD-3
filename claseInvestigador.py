from clasePersonal import Personal
    
class Investigador(Personal):
    __area: str
    __tipo: str
    
    def __init__(self, cuil = '', apellido = '', nombre = '', sueldo = 0.0, antiguedad = 0, area = '', tipo = ''):
        super().__init__(cuil, apellido, nombre, sueldo, antiguedad)
        self.__area = area
        self.__tipo = tipo
        
    def getArea(self):
        return self.__area
    
    def getTipo(self):
        return self.__tipo
    
    def getSueldo(self):
        sueldotot = super().getSueldoBasico() + (super().getSueldoBasico() * (super().getAntiguedad()/100))
        return sueldotot
    
    def __str__(self):
        return super().__str__()+ "\n Area de investigacion: " + self.__area + " Tipo de investigacion: " + self.__tipo