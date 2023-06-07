import json
from pathlib import Path
from claseColeccion import Coleccion
from claseNodo import Nodo
from claseApoyo import Apoyo
from claseDocente import Docente
from claseInvestigador import Investigador
from claseDocInv import DocenteInvestigador

class Decodificador(object):
    
    def decodificarDic(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'Coleccion':
                listaPersonal = class_()
                personal = d['Personal']
                for i in range(len(personal)):
                    dAgente = personal[i]
                    class_name = dAgente.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dAgente.pop('__atributos__')
                    unAgente = class_(**atributos)
                    listaPersonal.agregarElemento(unAgente)
        return listaPersonal
    
    def guardarJSON(self, diccionario, archivo):
        with Path(archivo).open('w', encoding = 'UTF-8') as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()
            
    def leerJSON(self, archivo):
        with Path(archivo).open(encoding= 'UTF-8') as fuente:
            diccionario = json.load(fuente)
            fuente.close()
            return diccionario