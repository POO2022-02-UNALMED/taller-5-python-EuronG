import gestion.zona
"""import zooAnimales.mamifero
import zooAnimales.ave
import zooAnimales.reptil
import zooAnimales.pez
import zooAnimales.anfibio"""
"""from gestion.zona import Zona
from zooAnimales.mamifero import Mamifero
from zooAnimales.ave import Ave
from zooAnimales.reptil import Reptil
from zooAnimales.pez import Pez
from zooAnimales.anfibio import Anfibio"""


class Animal(gestion.zona.Zona):
    _totalAnimales = 0
    mamiferos = 0
    aves = 0
    peces = 0
    reptiles = 0
    anfibios = 0

    def __init__(self, nombre, edad, habitat, genero, tipo=None):
        super().__init__(None, None)
        self._zona = None
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        Animal._totalAnimales += 1
        Animal._contador(tipo)

    @classmethod
    def _contador(cls, tipo):
        if tipo is None:
            return
        name = tipo.__class__.__name__
        if name == "Mamifero":
            cls.mamiferos += 1
        elif name == "Ave":
            cls.aves += 1
        elif name == "Reptil":
            cls.reptiles += 1
        elif name == "Pez":
            cls.peces += 1
        else:
            cls.anfibios += 1

    @classmethod
    def agganfibio(cls):
        cls.anfibios += 1

    @classmethod
    def aggave(cls):
        cls.aves += 1

    @classmethod
    def aggmamifero(cls):
        cls.mamiferos += 1

    @classmethod
    def aggpez(cls):
        cls.peces += 1

    @classmethod
    def aggreptil(cls):
        cls.reptiles += 1

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

    @classmethod
    def totalPorTipo(cls):
        return f"Mamiferos : {cls.mamiferos}\nAves : {cls.aves}\nReptiles : {cls.reptiles}\nPeces : {cls.peces}\nAnfibios : {cls.anfibios}"

    def __str__(self):
        if self._zona is None:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}"
        else:
            return f"Mi nombre es {self.getNombre()}, tengo una edad de {self.getEdad()}, habito en {self.getHabitat()} y mi genero es {self.getGenero()}, la zona en la que me ubico es {self.getZona().getNombre()}, en el zoo {self.getZona()[0].getZoo().getNombre()}"

    def toString(self):
        return self.__str__()