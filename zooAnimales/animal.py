from gestion.zoologico import Zoologico
from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio


class Animal(Zona):
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitat, genero):
        self._zona = None
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1

    @classmethod
    def getTotalAnimales(cls):
        return cls._totalAnimales

    @classmethod
    def setTotalAnimales(cls, animales):
        cls._totalAnimales = animales

    def getEdad(self):
        return self._edad

    def setEdad(self, edad):
        self._edad = edad

    def getHabitat(self):
        return self._habitat

    def setHabitat(self, habitat):
        self._habitat = habitat

    def getGenero(self):
        return self._genero

    def setGenero(self, genero):
        self._genero = genero

    def getZona(self):
        return self._zona

    def setZona(self, zona):
        self._zona = [zona]

    def movimiento(self):
        name = self.__class__.__name__
        if name == "Mamifero":
            return "desplazarse"
        elif name == "Ave":
            return "volar"
        elif name == "Reptil":
            return "reptar"
        elif name == "Pez":
            return "nadar"
        else:
            return "saltar"

    @staticmethod
    def totalPorTipo():
        return f"Mamiferos: {Mamifero.cantidadMamiferos()}\nAves: {Ave.cantidadAves()}\nReptiles: {Reptil.cantidadReptiles()}\nPeces: {Pez.cantidadPeces()}\nAnfibios: {Anfibio.cantidadAnfibios()} "

    def __str__(self):
        if self._zona is None:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}";
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona().getNombre()}, en el zoo {self.getZona()[0].getZoo().getNombre()}"

x = Animal("juan", 12, "selva", "m")
y = Animal("diego", 2, "selvis", "f")
w = x.__class__.__name__
print(w)