from gestion.zoologico import Zoologico


class Zona(Zoologico):
    def __init__(self, nombre, zoo):
        self._animales = None
        self._nombre = nombre
        self._zoo = [zoo]

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getZoo(self):
        return self._zoo

    def setZoo(self, zoo):
        self._zoo = [zoo]

    def getAnimales(self):
        return self._animales

    def setAnimales(self, animales):
        self._animales = animales

    def agregarAnimales(self, animal):
        if self._animales is None:
            self._animales = [animal]
        else:
            self._animales.append(animal)

    def cantidadAnimales(self):
        return len(self.getAnimales())

