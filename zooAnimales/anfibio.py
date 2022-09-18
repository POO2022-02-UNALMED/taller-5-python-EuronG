from zooAnimales.animal import Animal
from gestion.zona import Zona
from gestion.zoologico import Zoologico


class Anfibio(Animal):
    _listado = None
    ranas = 0
    salamandras = 0

    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super.__init__(nombre, edad, habitat, genero)
        self._colorPiel = colorPiel
        self._venenoso = venenoso

        if self._listado is None:
            self._listado = [self]
        else:
            self._listado.append(self)

    def getListado(self):
        return self._listado

    def setListado(self, listado):
        self._listado = listado

    def getColorPiel(self):
        return self._colorPiel

    def setColorPiel(self, color):
        self._colorPiel = color

    def isVenenoso(self):
        return self._venenoso

    def cantidadAnfibios(self):
        return len(self._listado)

    def crearRana(self, nombre, edad, genero):
        self.ranas += 1
        self.__init__(nombre, edad, "selva", genero, "rojo", True)

    def crearSalamandras(self, nombre, edad, genero):
        self.salamandras += 1
        self.__init__(nombre, edad, "selva", genero, "negro y amarillo", False)
